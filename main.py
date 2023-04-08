import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg")

with col2:
    st.title("Promodh")
    content = """Hi, I am Promodh. I am an undergraduate in IT from MIT.
    I am very much interested in Python and hoping to get more experience
    in data science and excel in it.
    """
    st.info(content)

