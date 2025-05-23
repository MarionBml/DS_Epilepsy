#modules nécéssaires

import streamlit as st

# création menu
intro_page = st.Page("1_intro.py", title="Introduction", icon="📖")
data_page = st.Page("2_donnees.py", title="Données", icon="🗂️")
analysis_page = st.Page("3_classification.py", title="Classification du problème", icon="📈")
visu_page = st.Page("4_visualisation.py",title="Visualisation", icon="👀")
preproc_page = st.Page("5_preprocessing.py", title="Preprocessing", icon="⚙️")
model_page = st.Page("6_modelisation.py", title="Modélisation", icon="⚖️")
pred_page = st.Page("7_prediction.py", title="Prédiction", icon="🔮")
conclu_page = st.Page("8_conclusion_et_perspectives.py", title="Conclusion et perspectives", icon="🥼")


#pg = st.navigation([intro_page, data_page, analysis_page, preproc_page, model_page, pred_page, conclu_page, perspective_page])
pg = st.navigation([intro_page, data_page, analysis_page, visu_page, preproc_page, model_page, pred_page, conclu_page])
st.set_page_config(page_title="Epilepsy project", page_icon=":material/edit:")
pg.run()

# sidebar
st.sidebar.title("Projet Epilepsie 📄")
with st.sidebar.expander("Notre équipe"):
    st.caption("[Manon Boyer 🦸‍♀️](https://www.linkedin.com/in/manonboyerphd/)")
    st.caption("[Paul Faucheux 🦸🏻‍♂️](https://www.linkedin.com/in/paul-faucheux-a876a741/)")
    st.caption("[Marion Lee 🦸‍♀️](https://www.linkedin.com/in/marion-lee-b00731971/)")


