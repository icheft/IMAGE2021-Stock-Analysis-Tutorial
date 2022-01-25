import streamlit as st
import io


def main():
    # Render the readme as markdown using st.markdown.
    readme_file = io.open("README.md", mode="r", encoding="utf-8")
    readme_text = st.markdown(readme_file.read(), unsafe_allow_html=True)
