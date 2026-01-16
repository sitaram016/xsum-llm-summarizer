# Text Summarization using LLM

## Overview
This project implements a simple text summarization web application using a Large Language Model (LLM).
The application allows a user to paste any long text (such as a news article) and get a concise summary.

The focus of this project is to demonstrate the overall GenAI pipeline and application workflow rather than building a highly optimized or production-ready model.

---

## Model Choice
For summarization, a pretrained LLM is used instead of training a model from scratch.
This decision was made to reduce complexity and execution time, and to focus on inference and system design.

Using a managed LLM API also avoids environment-specific issues related to heavy ML dependencies.

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
The web interface is built using **Streamlit**.
The application runs locally on the user’s system and opens in a browser.

---

## How to Run the Application Locally

### 1. Clone the repository
```bash
git clone https://github.com/sitaram016/xsum-llm-summarizer.git
cd xsum-llm-summarizer
