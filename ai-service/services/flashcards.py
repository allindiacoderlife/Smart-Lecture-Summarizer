def generate_flashcards(text):
    sentences = text.split(".")
    flashcards = []

    # Clean and filter sentences to create simple Q&A flashcards
    for s in sentences:
        s = s.strip()
        if len(s) > 30:
            flashcards.append({
                "question": f"Explain the concept: {s[:50]}...",
                "answer": s
            })
        
        if len(flashcards) >= 10:
            break

    return flashcards
