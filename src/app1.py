import requests
import streamlit as st

from mermaid import mermaid
from text import text

SERVER_URL = "http://127.0.0.1:8000"


def button1():
    if st.button("Get Data from FastAPI"):
        response = requests.get(f"{SERVER_URL}/api/data")
        st.write(f"response: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            st.write(data)
        else:
            st.write("Error: Unable to fetch data")


def button2():
    if st.button("Reset"):
        return None


# ページのコンテンツ
text.TITLE
button1()
button2()
mermaid(text.FIGURES[0], height=400)
with st.expander("About Streamlit"):
    st.write(text.DESCRIPTIONS[0])
with st.expander("About FastAPI"):
    st.write(text.DESCRIPTIONS[1].format(SERVER_URL=SERVER_URL))
