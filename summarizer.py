from transformers import pipeline

# Load model ONCE (global)
summarizer = pipeline(
    "summarization",
    model="facebook/bart-large-cnn"
)

def preprocess(text):
    return text.replace("\n", " ").strip()

def summarize_text(text):
    clean_text = preprocess(text)
    summary = summarizer(
        clean_text,
        max_length=130,
        min_length=30,
        do_sample=False
    )
    return summary[0]["summary_text"]
