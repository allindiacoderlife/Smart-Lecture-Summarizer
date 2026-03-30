import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

# Using Groq for high-quality, lightning-fast summarization
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def summarize_text(text):
    # Basic check to avoid errors on very short text
    if len(text.strip()) < 50:
        return text
        
    try:
        # Prompting for a structured, concise summary
        completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system", 
                    "content": "You are an expert academic summarizer. Provide a concise, structured summary of the following lecture material. Use bullet points for key takeaways."
                },
                {
                    "role": "user", 
                    "content": text
                }
            ],
            model="llama-3.3-70b-versatile",
            temperature=0.3,
            max_tokens=2048,
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"Summarization Error: {str(e)}"
