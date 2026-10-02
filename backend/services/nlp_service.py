import io
import PyPDF2
import spacy
from typing import List, Tuple
from fastapi import UploadFile
from utils.predefined_skills import get_skills_for_role

# Load spaCy model (ensure it's downloaded: python -m spacy download en_core_web_sm)
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    print("Warning: spaCy model 'en_core_web_sm' not found. Skill extraction may be less accurate.")
    print("Run: python -m spacy download en_core_web_sm")
    nlp = None

async def extract_text_from_file(file: UploadFile) -> str:
    """Extracts text from an uploaded file (PDF or TXT)."""
    content = await file.read()
    
    if file.filename.lower().endswith('.pdf'):
        pdf_reader = PyPDF2.PdfReader(io.BytesIO(content))
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text() + " "
        return text
    elif file.filename.lower().endswith('.txt'):
        return content.decode('utf-8')
    else:
        # Fallback to try decoding as utf-8
        try:
            return content.decode('utf-8')
        except UnicodeDecodeError:
            raise ValueError("Unsupported file format. Please upload a PDF or TXT file.")

def extract_skills(text: str, target_role: str) -> Tuple[List[str], List[str], float]:
    """
    Analyzes text to find existing skills based on the target role
    and identifies missing skills.
    """
    required_skills = get_skills_for_role(target_role)
    
    if not required_skills:
        # If no predefined skills, we can't do a proper gap analysis easily without an LLM
        # For this basic implementation, we'll return empty lists if role is unknown
        return [], [], 0.0

    text_lower = text.lower()
    
    # Simple keyword matching first
    found_skills = set()
    
    # Optionally use spaCy to lemmatize text for better matching
    if nlp:
        doc = nlp(text_lower)
        lemmatized_text = " ".join([token.lemma_ for token in doc])
    else:
        lemmatized_text = text_lower

    for skill in required_skills:
        if skill in lemmatized_text or skill in text_lower:
            found_skills.add(skill)
            
    existing_skills = list(found_skills)
    missing_skills = [skill for skill in required_skills if skill not in existing_skills]
    
    match_percentage = 0.0
    if required_skills:
        match_percentage = (len(existing_skills) / len(required_skills)) * 100
        match_percentage = round(match_percentage, 2)
        
    return existing_skills, missing_skills, match_percentage
