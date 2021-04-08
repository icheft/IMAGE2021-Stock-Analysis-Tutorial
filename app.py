import streamlit as st
import io
from src import draft, demo

MAGE_EMOJI_URL = "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/twitter/259/mage_1f9d9.png"

# Set page title and favicon
st.set_page_config(
    page_title="Advanced Python 課程", page_icon=MAGE_EMOJI_URL
)


def main():
    # Render the readme as markdown using st.markdown.
    readme_file = io.open("README.md", mode="r", encoding="utf-8")
    readme_text = st.markdown(readme_file.read())

    st.sidebar.title("模式切換")
    selector = ["課程大綱與說明", "初稿", '成果展示']
    app_mode = st.sidebar.selectbox("選擇教學簡介",
                                    selector)

    if app_mode == selector[0]:
        st.sidebar.success('課程說明文件')
    elif app_mode == selector[1]:
        readme_text.empty()
        st.sidebar.success('課程教學初稿')
        draft.main()
    elif app_mode == selector[2]:
        readme_text.empty()
        st.sidebar.success('Demo 一下')
        demo.main()


if __name__ == "__main__":
    main()
