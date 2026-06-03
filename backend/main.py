from fastapi import FastAPI
from backend.engine import ModelEngine
from pydantic import BaseModel

class TextRequest(BaseModel):
    request: str
    
RyuuLanguageEngine = ModelEngine()
Ryuu = FastAPI()

@Ryuu.post("/inputText")
def inputText(request: TextRequest):
    outputText = RyuuLanguageEngine.chatPrompt(request)
    return outputText