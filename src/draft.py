import streamlit as st
import io


def main():
    # Render the readme as markdown using st.markdown.
    readme_file = io.open("draft.md", mode="r", encoding="utf-8")
    readme_text = st.markdown(readme_file.read())
