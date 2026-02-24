from fastapi import FastAPI, UploadFile, File
import pdfplumber
import re
from skills import REQUIRED_SKILLS

app = FastAPI(title="AI Resume Checker")

def extract_text_from_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text.lower()

def check_skills(text):
    found = []
    missing = []

    for skill in REQUIRED_SKILLS:
        if skill in text:
            found.append(skill)
        else:
            missing.append(skill)

    score = int((len(found) / len(REQUIRED_SKILLS)) * 100)
    return found, missing, score

def detect_pii(text):
    emails = re.findall(r"\S+@\S+", text)
    phones = re.findall(r"\b\d{10}\b", text)
    return {"emails": emails, "phones": phones}

@app.post("/analyze")
async def analyze_resume(file: UploadFile = File(...)):
    text = extract_text_from_pdf(file.file)
    found, missing, score = check_skills(text)
    pii = detect_pii(text)

    return {
        "match_score": score,
        "skills_found": found,
        "skills_missing": missing,
        "pii_detected": pii
    }