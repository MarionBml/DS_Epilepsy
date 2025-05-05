'''
Conclusion du projet 
Lien entre les résultats obtenus et la problématique métier
'''

import streamlit as st

st.header("Conclusion")

st.write("""
Ce projet a permis de comparer différentes approches de classification pour la détection de crises d’épilepsie à partir de signaux audio, dans un contexte de données déséquilibrées. Après avoir testé des méthodes classiques de machine learning, des modèles pré-entraînés (Wav2Vec2), et des réseaux neuronaux convolutifs (CNN), ce sont les CNN appliqués à des segments de 2 secondes qui ont offert le meilleur compromis entre performances (F1-score = 0.79), robustesse au déséquilibre des classes, et efficacité computationnelle. Cette solution constitue aujourd’hui la base retenue pour la suite du projet.
""")

st.title('Conclusion du projet')
with st.expander("🙏🏼 :rainbow[Remerciements]"):
    st.markdown(""" À l'issue de notre projet, nous souhaitons exprimer notre gratitude envers les personnes qui ont soutenu notre travail. Leur contribution a été essentielle à la réalisation de cette étude.""")
    st.markdown("""Ainsi, nous tenons tout particulièrement à remercier chaleureusement :""")                
    st.markdown("""* 👨🏽‍⚕️ Dr Mario Chavez, à l'initiative de ce projet, pour sa généreuse fourniture des données anonymisées et annotées, indispensables à notre travail.""")
    st.markdown("""* 👨🏻‍⚕️ Dr Valerio Frazzini, qui a récolté, sélectionné et annoté les données, assurant ainsi leur qualité et leur pertinence pour notre étude.""")
    st.markdown("""* 👨🏻‍💻 Thomas Boehler, notre chef de cohorte et encadrant sur ce projet, pour sa guidance précieuse et son accompagnement lors de nos moments d'incertitude, en nous orientant vers les bonnes démarches.""")
    st.markdown("""* 👩🏽‍💻 Aïda, notre Program Manager, pour la gestion de la planification des réunions sur la plateforme DataScientest, facilitant ainsi le bon déroulement de notre formation.""")
    st.markdown("""Et enfin, un grand merci à l’ensemble de l’équipe de notre établissement de rattachement DataScientest.""")
