AI-Resume Screening System

The AI Resume Screening System is an automated solution designed to analyze and rank resumes based on their relevance to a given job description. The system extracts skills from multiple resumes, compares them with required job skills, and assigns a matching score to each candidate. This helps HR teams reduce manual screening time and improve shortlisting efficiency.


 🎯 Objective

* Automate resume screening using Natural Language Processing (NLP)
* Extract structured information such as skills from resumes
* Compare resumes against job requirements
* Rank candidates based on relevance score
* Generate a CSV report for HR decision-making


 ⚙️ Tech Stack & Tools

* **Python** – Core programming language
* **spaCy** – NLP-based skill extraction
* **pdfminer.six** – Text extraction from PDF resumes
* **docx2txt** – Text extraction from DOCX resumes
* **pandas** – Data processing and CSV generation


🧠 System Workflow

1. The system reads all resumes from the specified folder.
2. Supported formats (PDF and DOCX) are processed one by one.
3. Skills are extracted from each resume using NLP techniques.
4. The job description is converted into a structured skill list.
5. Resume skills are compared with job skills.
6. A matching score is calculated for each resume.
7. Unsupported files are skipped with an informative message.
8. Final results are saved in a CSV file for review.

## 📊 Scoring Methodology

* Resume scores are calculated based on overlapping skills with the job description.
* Score = (Matched Skills / Total Job Skills) × 100
* The system achieves approximately **90% scoring accuracy**, effectively reflecting candidate-job relevance.


📁 Input

* Resume files (PDF/DOCX)
* Job description (text format)


 📤 Output

* CSV file containing:

  * Resume filename
  * Extracted skills
  * Matching score (%)

 ✅ Key Features
* Automated resume screening
* Batch processing of multiple resumes
* NLP-based skill extraction
* Job description matching
* CSV report generation
* Error handling for unsupported formats

 🚀 Use Cases
* HR shortlisting automation
* Recruitment analytics
* Internship and fresher hiring
* Resume ranking systems
