import os
from sentence_transformers import SentenceTransformer
import numpy as np
import sqlite3
import faiss

CHUNK_SIZE = 500
CHUNK_OVERLAP = 50
EMBED_MODEL = "paraphrase-multilingual-MiniLM-L12-v2"
DB_PATH = "data/ryuu.db"
INDEX_PATH = "data/ryuu.index"

def chunkLoader(inDoc):
    with open (inDoc, "r", encoding="utf-8") as ragFile:
        fileTextFull = ragFile.read()

    fileWords = fileTextFull.split()
    chunkStart = 0
    chunks = []
    while chunkStart < len(fileWords):
        chunkEnd = chunkStart + CHUNK_SIZE
        chunk = " ".join(fileWords[chunkStart:chunkEnd])
        chunks.append(chunk)
        chunkStart += CHUNK_SIZE - CHUNK_OVERLAP

    return chunks

def ryuuEmbed(chunkList):
    embedder = SentenceTransformer(EMBED_MODEL)
    embedVector = embedder.encode(chunkList)
    return embedVector

def ryuuDB(chunkIn, vectorIn):
    dbConnection = sqlite3.connect(DB_PATH)
    dbConnection.execute("""
        CREATE TABLE IF NOT EXISTS chunks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        chunk_text TEXT
        )
    """)
    dbConnection.commit()
    for dbIndex in chunkIn:
        dbConnection.execute(
            "INSERT INTO chunks (chunk_text) Values (?)",
            (dbIndex,)
        )
    dbConnection.commit()

    vectors = np.array(vectorIn).astype("float32")
    index = faiss.IndexFlatIP(vectors.shape[1])
    faiss.normalize_L2(vectors)
    index.add(vectors)
    faiss.write_index(index, INDEX_PATH)
    dbConnection.close() 

def ryuuRetrieve(userInput):
    if not os.path.exists(INDEX_PATH):
        return ""

    retriever = SentenceTransformer(EMBED_MODEL)
    retrieveVector = retriever.encode(userInput)
    retreiveIndex = faiss.read_index(INDEX_PATH)
    retrieveVector = np.array([retrieveVector]).astype("float32")
    faiss.normalize_L2(retrieveVector)
    vectorMatch, ids = retreiveIndex.search(retrieveVector, 2)
    dbConnection = sqlite3.connect(DB_PATH)
    retrievedChunks = []
    for dbIndex in ids[0]:
        result = dbConnection.execute(
            "SELECT chunk_text FROM chunks WHERE id = ?",
            (int(dbIndex) + 1,)
        ).fetchone()
        retrievedChunks.append(result[0])

    dbConnection.close()
    return "\n\n".join(retrievedChunks)

def ryuuIngest(inDoc):
    chunks = chunkLoader(inDoc)
    vectors = ryuuEmbed(chunks)
    ryuuDB(chunks, vectors)    