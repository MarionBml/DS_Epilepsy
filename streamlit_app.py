import streamlit as st


intro_page = st.Page("1_intro.py", title="Introduction", icon="📖")
data_page = st.Page("2_donnees.py", title="Données", icon="🗂️")


pg = st.navigation([intro_page, data_page])
st.set_page_config(page_title="Epilepsy project", page_icon=":material/edit:")
pg.run()

st.sidebar.title("Projet Epilepsie 📄")
with st.sidebar.expander("Notre équipe"):
    st.caption("[Manon Boyer 🦸‍♀️](https://www.linkedin.com/in/manonboyerphd/)")
    st.caption("[Paul Faucheux 🦸🏻‍♂️](https://www.linkedin.com/in/paul-faucheux-a876a741/)")
    st.caption("[Marion Lee 🦸‍♀️](https://www.linkedin.com/in/marion-lee-b00731971/)")

with st.sidebar.expander("Remerciements"):
    st.markdown(""" À l'issue de notre projet, nous souhaitons exprimer notre gratitude envers les personnes qui ont soutenu notre travail. Leur contribution a été essentielle à la réalisation de cette étude.""")
    st.markdown("""Ainsi, nous tenons tout particulièrement à remercier chaleureusement :""")                
    st.markdown("""* Dr Mario Chavez, à l'initiative de ce projet, pour sa généreuse fourniture des données anonymisées et annotées, indispensables à notre travail.""")
    st.markdown("""* Dr Valerio Frazzini, qui a récolté, sélectionné et annoté les données, assurant ainsi leur qualité et leur pertinence pour notre étude.""")
    st.markdown("""* Thomas Boehler, notre chef de cohorte et encadrant sur ce projet, pour sa guidance précieuse et son accompagnement lors de nos moments d'incertitude, en nous orientant vers les bonnes démarches.""")
    st.markdown("""* Aïda, notre Program Manager, pour la gestion de la planification des réunions sur la plateforme DataScientest, facilitant ainsi le bon déroulement de notre formation.""")
    st.markdown("""Et enfin, un grand merci à l’ensemble de l’équipe de notre établissement de rattachement DataScientest.""")