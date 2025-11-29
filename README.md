# Parallel Text Processing - Sentiment Analysis  
### Developed by **Srinivas**

This repository contains the complete implementation of the **Parallel Text Processing Pipeline** built as part of the Springboard Internship Program.  
The project focuses on large-scale text preprocessing, parallel sentiment analysis, and an interactive UI using Streamlit.

---

## 📌 Project Overview

The goal of this project is to create a **high-performance, scalable text analysis system** that can handle thousands of tweets efficiently.  
The system supports:

- Text cleaning  
- NLP normalization  
- Rule-based and transformer-based sentiment analysis  
- Multiprocessing for performance  
- SQLite storage  
- CSV export  
- Automated email summary  
- Streamlit-based UI for demos  

All features are implemented across **four milestones**, each documented in the final PDF.

---

## 🧩 Features

### ✔ **1. Data Ingestion**
- Load CSV dataset  
- Store data into SQLite database  

### ✔ **2. Text Processing**
- Lowercasing, emoji removal, regex cleanup  
- Tokenization  
- Lemmatization  
- Stopword filtering (spaCy)  

### ✔ **3. Parallel Processing**
- Word-count multiprocessing  
- Parallel sentiment classification using Hugging Face  

### ✔ **4. Sentiment Analysis**
- **TextBlob** (rule-based)  
- **Twitter-RoBERTa** transformer (HuggingFace)  

### ✔ **5. Results & Visualization**
- CSV export  
- Confusion matrix comparison  
- Performance benchmarking  

### ✔ **6. Email Automation**
- Sends sentiment summary through Gmail SMTP  
- Includes CSV attachment  

### ✔ **7. Streamlit UI**
- Single text input  
- Batch file upload  
- Sequential/parallel sentiment options  
- Output preview & CSV download  
- Email summary trigger  

---

## 📁 Project Structure
├── data/
│ └── tweets.csv (or your dataset)
├── notebooks/
│ ├── SRINIVAS_MILESTONE-1.ipynb
│ ├── SRINIVAS_MILESTONE-2.ipynb
│ ├── MILESTONE-3-SRINIVAS.ipynb
│ └── IntershipProject.ipynb (Milestone 4)
├── app.py (Streamlit UI)
├── utils.py (Optional helper functions)
├── requirements.txt
└── Documentation.pdf <-- Final PDF documentation


---

## 📚 Full Documentation (Recommended for Review)

A complete milestone-wise technical documentation (including code, workflow, design, and explanations) is available in the PDF:

👉 **Please refer to the PDF file `_Parallel_Text_Processing_Documentation.pdf_` for complete details of this project.**  
This PDF is suitable for:

- Interview presentation  
- Internship review  
- Project submission  
- Academic or professional portfolio  

---

## 🔧 Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/SRINIVASRAOAMMANGOD/Parallel-Text-Processing-Project.git
cd Parallel-Text-Processing-Project
