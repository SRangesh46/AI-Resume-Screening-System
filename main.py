import os
import pandas as pd
import spacy
from pdfminer.high_level import extract_text
import docx2txt

# -------------------- STEP 0: Paths --------------------
resume_folder = r"C:\Users\range\Ai resume screening projects\resumes"
output_csv = r"C:\Users\range\Ai resume screening projects\resume_scores.csv"

# -------------------- STEP 1: Load NLP model --------------------
nlp = spacy.load("en_core_web_sm")

# -------------------- STEP 2: Job Description --------------------
job_description = """
We are looking for a Data Scientist with strong Python, Machine Learning,
Deep Learning, and NLP skills. Minimum 2 years experience in Python and ML.
"""

def extract_skills(text):
    doc = nlp(text)
    return list(set([
        token.text.lower()
        for token in doc
        if token.pos_ in ["NOUN", "PROPN"] and len(token.text) > 1
    ]))

job_skills = extract_skills(job_description)
print("Job Skills:", job_skills)

# -------------------- STEP 3: Resume Text Extraction --------------------
def extract_resume_text(file_path):
    if file_path.endswith(".pdf"):
        return extract_text(file_path)
    elif file_path.endswith(".docx"):
        return docx2txt.process(file_path)
    else:
        return None  # unsupported file

# -------------------- STEP 4: Resume Scoring --------------------
def score_resume(resume_skills, job_skills):
    if not resume_skills:
        return 0
    matched = set(resume_skills).intersection(set(job_skills))
    return round((len(matched) / len(job_skills)) * 100, 2)

# -------------------- STEP 5: Process ALL resumes --------------------
results = []

for file in os.listdir(resume_folder):
    file_path = os.path.join(resume_folder, file)
    print(f"\nProcessing resume: {file}")

    # Unsupported format
    if not (file.endswith(".pdf") or file.endswith(".docx")):
        print(f" Unsupported file format: {file}")
        results.append({
            "filename": file,
            "score": "Not Supported",
            "status": "Unsupported format"
        })
        continue

    try:
        text = extract_resume_text(file_path)

        if not text or not text.strip():
            print(f"️ No readable text found in: {file}")
            results.append({
                "filename": file,
                "score": 0,
                "status": "Empty / unreadable resume"
            })
            continue

        resume_skills = extract_skills(text)
        score = score_resume(resume_skills, job_skills)

        results.append({
            "filename": file,
            "score": score,
            "status": "Processed"
        })

        print(f"✅ Score for {file}: {score}%")

    except Exception as e:
        print(f" Error processing {file}: {e}")
        results.append({
            "filename": file,
            "score": "Error",
            "status": str(e)
        })

# -------------------- STEP 6: Save results to CSV --------------------
df_results = pd.DataFrame(results)
df_results.to_csv(output_csv, index=False)

print("\n✅ Resume screening completed")
print(f" Results saved to: {output_csv}")
