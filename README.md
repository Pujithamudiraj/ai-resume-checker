# AI Resume Screening & Compliance Checker

An enterprise-style, rule-based AI system designed to analyze resumes against predefined job requirements and detect Personally Identifiable Information (PII) for compliance and governance purposes.

---

## 📌 Executive Summary

This project simulates a real-world AI screening system used in recruitment pipelines. It performs:

- Resume parsing from PDF
- Skill matching against job requirements
- Match score generation
- PII detection for compliance (GDPR-style awareness)
- REST API-based microservice architecture

The system is lightweight, cloud-ready, and designed using scalable backend principles.

---

## 🏗 System Architecture Overview

Resume (PDF Upload)  
⬇  
Text Extraction (pdfplumber)  
⬇  
Rule-Based Skill Matching Engine  
⬇  
PII Detection Module (Regex-based)  
⬇  
REST API Response (FastAPI JSON Output)

This modular design makes the system extensible and cloud-deployable.

---

## 🧠 Core Functionalities

### 1️⃣ Resume Text Extraction
- Extracts content from uploaded PDF resumes
- Normalizes text for processing

### 2️⃣ Skill Matching Engine
- Compares resume content against predefined required skills
- Calculates match score percentage
- Identifies:
  - Skills Found
  - Skills Missing

### 3️⃣ PII Detection & Compliance
- Detects:
  - Email addresses
  - Phone numbers
- Demonstrates awareness of:
  - Data Governance
  - Privacy Compliance (GDPR-style principles)

### 4️⃣ REST API Interface
- Built using FastAPI
- Swagger UI available for testing
- JSON-based structured output

---

## 🛠 Technology Stack

- Python 3.11
- FastAPI
- Uvicorn
- pdfplumber
- Regular Expressions (PII detection)
- Git & GitHub
- Cloud-ready architecture (AWS deployable)

---

## 📂 Project Structure

```
ai-resume-checker/
│
├── main.py              # FastAPI application
├── skills.py            # Skill database
├── requirements.txt     # Dependencies
├── README.md
└── .gitignore
```

---

## ⚙️ Local Setup Instructions

### 1. Clone Repository

```
git clone https://github.com/YOUR_USERNAME/ai-resume-checker.git
cd ai-resume-checker
```

### 2. Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```
pip install -r requirements.txt
```

### 4. Run Application

```
uvicorn main:app --reload
```

### 5. Access Swagger UI

```
http://127.0.0.1:8000/docs
```

## ☁️ Cloud Deployment Readiness

The application is designed to be deployed using:

- AWS EC2 (Free Tier)
- Azure Virtual Machines
- Docker Containers
- Reverse Proxy with Nginx

Security considerations include:
- Role-based access (IAM in cloud)
- Secure API exposure
- Environment isolation

---

## 🔐 Data Governance Considerations

- Sensitive information detection
- Structured JSON output
- Modular architecture for future compliance extensions
- Ready for integration with secure cloud storage

---

## 🚀 Future Enhancements

- Add database integration (PostgreSQL)
- Add frontend UI dashboard
- Implement embeddings-based semantic matching
- Add authentication & authorization
- Containerize using Docker
- Add logging & monitoring


- Git workflow and version control
