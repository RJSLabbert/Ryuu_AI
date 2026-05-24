\#Ryuu 竜 🐉

\*\*Local AI Dragon\*\*

Ryuu is essentially a Raspberry Pi5 equipped with a Hailo 10H NPU running AI locally. It evolved into a proof of concept of Running AI locally and scalable for enterprises. Ryuu is a FastAPI python inference using HailoRT and the NPU with a RAG system, and possible internet access for research and updates. The Successor of \[FARA](https://github.com/RJSLabbert/fara-ai).

\[!\[Python](https://img.shields.io/badge/Python-3.13+-blue?logo=python\&logoColor=white)](https://python.org)

\[!\[FastAPI](https://img.shields.io/badge/FastAPI-backend-green?logo=fastapi\&logoColor=white)](https://fastapi.tiangolo.com)

\[!\[HailoRT](https://img.shields.io/badge/HailoRT-5.1.1-blue?)](https://github.com/hailo-ai/hailort)

\[!\[Status](https://img.shields.io/badge/Status-Active\_Development-orange?style=flat-square)](https://github.com/RJSLabbert/Ryuu\_AI)

\---

\##Why I built this

I wanted to build my own AI. Not use someone else's API, not pay for cloud tokens. Actually build something that runs entirely on my own hardware. FARA was the proof of concept. Ryuu is the answer to that. A local AI dragon with an animated character, emotion states wired to the backend, and a Raspberry Pi 5 as his dedicated hardware home. This is the answer to that curiosity, a fully local FastAPI application on a raspberry pi and NPU inference. Using HailoRT and python I am setting out to create a proof of concept on a scale that works with the Raspberry Pi5.The only limit is the Hardware. 

\---

\## ✨ Features

\### 🖥️ Local AI Core

\-Runs on local Hardware, no cloud or API tokens used.

\-FastAPI and HailoRT on local NPU.

\### 💬 Input

\-Input is text based.

\-Tokenizes text input then converted for processing on the NPU.

\-Future RAG system implementation.

\---

\## 🛠️ Tech Stack

\-Python 3.13+

\-FastAPI

\-HailoRT 5.1.1

\-Linux bash

\-Hailo 10H NPU 

\---

\## 🚀 Quick Setup (Linux)

1. Clone the repo:

&#x09;```bash

&#x09;git clone https://github.com/RJSLabbert/Ryuu\_AI

&#x09;```

2\. Go to directory:

&#x09;```bash

&#x09;cd /Ryuu\_AI/

&#x09;```

3\. Create and activate Python Venv(Safety for testing):

&#x09;```bash

&#x09;python3 -m venv venv \&\& source venv/bin/activate

&#x09;```

4\. Install dependencies:

&#x09;```bash

&#x09;pip install -r requirements.txt

&#x09;```

5\. Run main.py

&#x09;```bash

&#x09;python3 main.py

&#x09;```

\---

\## 📁 Project Structure

```

Ryuu\_AI/

├── LICENSE

├── README.md

├── requirements.txt

├── .gitignore

├── backend/

│   ├── engine.py

│   └── main.py

├── config/

│   └── .env

└── models/

```

\---

\## 👤 Author

\*\*RJ SLabbert\*\*



\- GitHub: \[@RJSLabbert](https://github.com/RJSlabbert)

\- Blog: \[rocksolidcode.co.za](https://rocksolidcode.co.za)



\---	

