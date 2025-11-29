# Parallel-Text-Processing-Project
A concurrent text processor built with Streamlit and Python multiprocessing. Analyzes sentiment using a Hugging Face LLM vs. TextBlob, with performance benchmarking, interactive filtering, and export options (CSV, DB, Email).
---
# Sentiment Analysis Application

This is an interactive web application built with Streamlit that provides a comprehensive platform for text sentiment analysis. It allows users to upload batch data, run analysis using both advanced AI (LLM) and traditional (TextBlob) methods, and benchmark the performance of sequential vs. parallel processing.

This project fulfills the requirements of a concurrent text processor, handling large batch datasets, running simultaneous analyses, providing database storage, and offering email/CSV summaries, all within a user-friendly, code-free interface.
---

## ✨ Key Features

* **Interactive UI:** Built with Streamlit for a clean, responsive user experience.
* **Quick Analysis:** A text box for instant sentiment analysis of a single sentence.
* **Batch Processing:** Upload `.csv` or `.xlsx` files for batch analysis via drag-and-drop or browsing.
* **Flexible Configuration:**
    * Automatically detects and lets you select the correct text column.
    * Provides both a **drag-slider** and a **manual number input** to select the number of rows to analyze.
* **Dual-Model Analysis:**
    * **Hugging Face LLM:** Uses the `cardiffnlp/twitter-roberta-base-sentiment-latest` model for high-accuracy, context-aware sentiment (Positive, Negative, Neutral) and provides a **Confidence Score**.
    * **TextBlob:** Uses a fast, rule-based approach to provide a comparative sentiment and a **Subjectivity Score** (0.0 Objective to 1.0 Subjective).
* **Performance Benchmarking:**
    * Runs the LLM analysis in two modes: **Sequential** (single-core) and **Parallel** (using `multiprocessing` on all available CPU cores).
    * Displays the execution time for both and calculates the **Speedup Factor**.
    * Includes "Performance Notes" to explain the trade-offs of parallel overhead vs. analysis speed.
* **Interactive Visualizations:**
    * **Toggle-able Charts:** Users can check boxes to show/hide:
        * **Agreement Heatmap:** Compares LLM vs. TextBlob predictions.
        * **Distribution Bar/Pie Chart:** Shows the breakdown of sentiments.
        * **Disagreement Bar Chart:** Visualizes what the LLM predicted when TextBlob disagreed.
* **"Searchable Lists" (Filtering):**
    * A detailed, filterable results table.
    * Users can filter by sentiment (e.g., show only "Negative" tweets).
    * Users can filter to show **only disagreements** between the two models.
* **Data Export Options:**
    * **Save to Database:** Saves the final results to an `SQLite` database file.
    * **Download Database:** A download button appears to download the `.db` file.
    * **Download CSV:** Download a clean `.csv` file of the results.
    * **Email Report:** Send the CSV as an email attachment directly from the app.

---

## 🛠️ Technology Stack

* **Core Framework:** Streamlit
* **Parallel Processing:** Python `multiprocessing` (`Pool`, `cpu_count`)
* **Advanced AI (LLM):** Hugging Face `transformers`
* **Rule-Based Analysis:** `TextBlob`
* **Data Handling:** Pandas, NumPy
* **Database:** SQLite3
* **Visualization:** Matplotlib, Seaborn
* **Export:** smtplib, email
* **Deployment:** Hugging Face Spaces (or Google Colab + Ngrok for demo)

---



## 🧠 Core Concepts Explained

### Performance: Parallel vs. Sequential
* **Sequential:** Analyzes one text at a time. It has a **low setup cost** (loads the 500MB+ model once) but is **slow to analyze** (e.g., 1000 texts * 0.1s/text = 100s).
* **Parallel:** Splits the data across all CPU cores. It has a **high setup cost** (each core loads its *own* 500MB+ model copy into RAM) but is **fast to analyze** (e.g., (1000 texts / 8 cores) * 0.1s/text = 12.5s).
* **Result:** Parallel is slower for small datasets (where setup cost dominates) but much faster for large datasets (where analysis time dominates).

### Analysis: LLM vs. TextBlob
* **LLM (Transformers):** A deep learning model that understands **context**. It knows "not good" is negative. It provides a **Confidence Score** (e.g., 98% sure it's Negative).
* **TextBlob (Rule-Based):** A simple library that uses a dictionary of word scores. It's very fast but can be easily confused by sarcasm or negation. It provides a **Subjectivity Score** (0.0 = fact, 1.0 = opinion), which the LLM does not.
