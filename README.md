# Text Summarization using LLM

## Overview
This project implements a simple text summarization web application using a Large Language Model (LLM).
The application allows a user to paste any long text (such as a news article) and get a concise summary.

The focus of this project is to demonstrate the overall GenAI pipeline and application workflow rather than building a highly optimized or production-ready model.

---

## Model Choice
For summarization, a pretrained Large Language Model is used instead of training a model from scratch.
This reduces complexity and execution time and allows the focus to remain on inference and system design.

A managed LLM API is used to avoid environment-specific issues related to heavy machine learning dependencies.

---

## Data
The application works with any text input provided by the user.
During development, news-style datasets from Hugging Face (such as XSum or CNN/DailyMail) were referred to for understanding summarization tasks.

---

## Preprocessing
Only minimal preprocessing is applied:
- Removal of unnecessary newlines
- Trimming extra spaces

This is sufficient because modern LLMs are robust to raw text input.

---

## Application Flow
1. User enters text in the web interface  
2. Text is passed to the summarization function  
3. LLM generates a concise summary  
4. Summary is displayed in the browser  

---

## Web Application
The web application is built using **Flask**.
It runs locally on the user’s system and can be accessed through a browser using a local URL.

---

## How to Run the Application Locally

1. **Clone the repository**

   ```bash
   git clone https://github.com/sitaram016/xsum-llm-summarizer.git
   cd xsum-llm-summarizer


2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**

   Create a `.env` file in the project directory and add your OpenAI API key:

   ```env
   OPENAI_API_KEY=your_api_key_here
   ```

4. **Run the web application**

   ```bash
   python app.py
   ```

5. **Open in browser**

   After running the command, open the following URL in your browser:

   ```
   http://127.0.0.1:5000
   ```

   Paste any text and click **Summarize** to view the output.

---

## Notes

* The `.env` file is excluded from version control to keep API keys secure.
* This project is intended for demonstration and evaluation purposes.

```
```

