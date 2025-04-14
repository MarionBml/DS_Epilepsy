import streamlit as st


intro_page = st.Page("1_intro.py", title="Introduction", icon="📖")
data_page = st.Page("2_data.py", title="Data", icon="🗂️")


pg = st.navigation([intro_page, data_page])
st.set_page_config(page_title="Epilepsy project", page_icon=":material/edit:")
pg.run()

st.sidebar.title("Epilepsy project📄")
with st.sidebar.expander("Our Team"):
    st.caption("[Manon Boyer 🦸‍♀️](https://www.linkedin.com/in/manonboyerphd/)")
    st.caption("[Paul Faucheux 🦸🏻‍♂️](https://www.linkedin.com/in/paul-faucheux-a876a741/)")
    st.caption("[Marion Lee 🦸‍♀️](https://www.linkedin.com/in/marion-lee-b00731971/)")