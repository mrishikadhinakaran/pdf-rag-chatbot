from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Allow CORS so frontend (localhost:5173) can talk to backend (localhost:8000)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # In production, replace with specific frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request model for chat
class ChatRequest(BaseModel):
    query: str

# In-memory chat history (temporary storage)
chat_history: List[str] = []

# ✅ Chat Endpoint
@app.post("/chat")
async def chat(request: ChatRequest):
    user_query = request.query
    response_text = f"Backend received: {user_query}"
    
    # Store in chat history
    chat_history.append(f"user: {user_query}")
    chat_history.append(f"bot: {response_text}")
    
    return {"response": response_text}

# ✅ File Upload Endpoint
@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    # You can add processing logic here later
    return {"filename": file.filename, "status": "Uploaded successfully"}

# ✅ History Endpoint
@app.get("/history")
async def get_history():
    return {"history": chat_history}

# ✅ Root Endpoint
@app.get("/")
async def root():
    return {"message": "✅ PDF Chatbot Backend is running 🚀"}
