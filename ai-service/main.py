from fastapi import FastAPI
from routes.process import router as process_router
from routes.chat import router as chat_router

app = FastAPI(title="Smart Lecture Summarizer AI Service")

app.include_router(process_router, prefix="/api")
app.include_router(chat_router, prefix="/api")

@app.get("/")
def home():
    return {"message": "AI Service Running"}
