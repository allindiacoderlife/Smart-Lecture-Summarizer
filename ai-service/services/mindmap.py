import spacy

# Load the small English NLP model
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    # Fallback if model isn't downloaded yet (handled in requirements/setup)
    import os
    os.system("python -m spacy download en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

def extract_keywords(text):
    doc = nlp(text)
    # Extract unique nouns and proper nouns for the mind map
    keywords = list(set([
        token.text for token in doc 
        if token.pos_ in ["NOUN", "PROPN"] and len(token.text) > 2
    ]))
    return keywords[:20] # Limit to top 20 keywords for readability
