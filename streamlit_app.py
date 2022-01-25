import streamlit as st
import io
from src import draft, demo, readme
from src import pws
from typing import Callable

PAGE_PARAM = "p"
CONTENT = {"doc": readme.main, "metrics": draft.main, "demo": demo.main}
LONG_TO_SHORT = {"課程大綱與說明": "doc", "評分標準": "metrics", "成果展示": "demo"}

MAGE_EMOJI_URL = "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/twitter/259/mage_1f9d9.png"

# Set page title and favicon
st.set_page_config(page_title="Advanced Python 課程", page_icon=MAGE_EMOJI_URL)


def main():
    query_params = st.experimental_get_query_params()
    page_param = query_params[PAGE_PARAM][0] if PAGE_PARAM in query_params else "doc"

    page_selected = None

    index = 0
    cur_index = 0
    for page_name, page_function in CONTENT.items():
        st.session_state[page_name] = page_name == page_param
        if st.session_state[page_name]:
            index = cur_index
        # print(st.session_state[page_name])
        cur_index += 1

    st.sidebar.title("模式切換")
    selector = LONG_TO_SHORT.keys()
    page_selected = st.sidebar.selectbox("選擇教學簡介", selector, index)

    # if page_selected in st.session_state and st.session_state[page_selected]:
    #     query_params = st.experimental_get_query_params()
    #     query_params[PAGE_PARAM] = page_selected
    #     print(query_params)

    #     st.experimental_set_query_params(**query_params)

    if page_selected:
        query_params[PAGE_PARAM] = LONG_TO_SHORT[page_selected]
        st.experimental_set_query_params(**query_params)

    page_function = CONTENT[LONG_TO_SHORT[page_selected]]
    if isinstance(page_function, Callable):
        # st.sidebar.success(page_selected)
        page_function()

    # if app_mode == selector[0]:
    #     readme.main()
    # elif app_mode == selector[1]:
    #     # readme_text.empty()
    #     st.sidebar.success("評分標準")
    #     draft.main()
    # elif app_mode == selector[2]:
    #     # readme_text.empty()
    #     st.sidebar.success("Demo 範例參考")
    #     demo.main()


if __name__ == "__main__":
    main()
