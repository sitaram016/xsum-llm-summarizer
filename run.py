# run.py
from summarizer import summarize_text

if __name__ == "__main__":
    text = input("Enter text to summarize:\n")
    summary = summarize_text(text)
    print("\nSummary:\n")
    print(summary)
