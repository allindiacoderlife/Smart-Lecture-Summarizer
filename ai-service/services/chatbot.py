import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

# Ensure you have GROQ_API_KEY in your .env file
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def get_response(question):
    try:
        # Using Llama 3 for fast, high-quality responses
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system", 
                    "content": "You are a helpful, brilliant AI tutor for students. Explain concepts in a simple, engaging, and clear way based on the lecture material."
                },
                {
                    "role": "user", 
                    "content": question
                }
            ],
            model="llama-3.3-70b-versatile",
            temperature=0.5,
            max_tokens=1024,
            top_p=1,
            stop=None,
            stream=False,
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"Groq AI Service Error: {str(e)}"
