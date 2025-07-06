from summarizer.ai import summarize
import streamlit as st


st.title("🌐 AI Website Summarizer")
url = st.text_input("Enter website URL", placeholder="https://example.com")

if st.button("Summarize"):
    if not url:
        st.warning("Please enter a valid URL.")
    else:
        with st.spinner("Summarizing..."):
            summary = summarize(url)
        st.markdown("## 📄 Summary")
        st.markdown(summary)


