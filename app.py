from flask import Flask, request
from summarizer import summarize_text

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    summary = ""
    if request.method == "POST":
        text = request.form.get("text", "")
        if text.strip():
            summary = summarize_text(text)

    return f"""
    <html>
        <head>
            <title>Text Summarization App</title>
        </head>
        <body>
            <h2>Text Summarization using LLM</h2>
            <form method="post">
                <textarea name="text" rows="10" cols="80"
                    placeholder="Paste text here"></textarea><br><br>
                <button type="submit">Summarize</button>
            </form>
            <h3>Summary</h3>
            <p>{summary}</p>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=False)
