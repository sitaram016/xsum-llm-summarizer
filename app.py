import streamlit as st
from summarizer import summarize_text

st.set_page_config(page_title="Text Summarization using LLM")

st.title("📰 Text Summarization using LLM")

text = st.text_area("Paste any news article or long text here")

if st.button("Summarize"):
    if text.strip():
        with st.spinner("Generating summary..."):
            summary = summarize_text(text)
        st.subheader("Summary")
        st.write(summary)
    else:
        st.warning("Please enter some text.")
