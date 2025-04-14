import streamlit as st

intro_page = st.Page("1_intro.py", title="Introduction", icon="📖")
data_page = st.Page("2_data.py", title="Data", icon="🗂️")

pg = st.navigation([intro_page, data_page])
st.set_page_config(page_title="Data manager", page_icon=":material/edit:")
pg.run()
