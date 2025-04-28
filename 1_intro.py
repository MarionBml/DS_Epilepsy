'''
Présentation du sujet, du problème et des enjeux

'''
import streamlit as st

st.title('Introduction')
st.subheader('Présentation du sujet')

st.subheader('Méthodes de détection des crises')

st.subheader('Détection des crises par l\'audio')

st.subheader('Objectifs')
st.markdown("""Les principaux objectifs de ce projet sont :""")
with st.expander(" 👨🏿‍⚕️Explorer la faisabilité de la détection des crises épileptiques à partir d'enregistrements audio"):
    st.caption("""L'objectif principal est d'analyser si les caractéristiques sonores des crises épileptiques, 
               telles que les variations de fréquence et les bruits spécifiques, peuvent être utilisées pour leur détection.""")
with st.expander(" 🕵️ Développer un système de détection basé sur l'analyse audio"):
    st.caption("""L'objectif est d’utiliser des algorithmes d’apprentissage automatique pour classifier 
               les crises et les périodes sans crise à partir des données audio collectées, 
               offrant ainsi une solution non invasive, confortable et accessible pour les patients.""")
with st.expander(" 👷🏽‍♀️ Poser les bases pour de futurs développements"):
    st.caption("""Cette étude sert de point de départ pour de futures avancées technologiques dans le domaine 
               de la détection des crises épileptiques, en évaluant les performances des algorithmes d’apprentissage
                automatique appliqués aux données audio et en identifiant les pistes d’amélioration possibles.""")