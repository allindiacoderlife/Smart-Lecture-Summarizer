from fastapi import APIRouter
from pydantic import BaseModel
from services.transcription import transcribe_audio
from services.summarization import summarize_text
from services.flashcards import generate_flashcards
from services.mindmap import extract_keywords

router = APIRouter()

class ProcessRequest(BaseModel):
    filePath: str

@router.post("/process")
def process_lecture(req: ProcessRequest):
    # 🎤 Audio -> Text (Transcription)
    text = transcribe_audio(req.filePath)
    
    # ✨ Text -> Summary
    summary = summarize_text(text)
    
    # 🧠 Text -> Flashcards
    flashcards = generate_flashcards(text)
    
    # 🗺️ Text -> Keywords for Mind Map
    keywords = extract_keywords(text)

    return {
        "transcript": text,
        "summary": summary,
        "flashcards": flashcards,
        "mindmap": keywords
    }
