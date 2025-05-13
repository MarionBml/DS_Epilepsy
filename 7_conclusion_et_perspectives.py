'''
Conclusion du projet 
Lien entre les résultats obtenus et la problématique métier
'''

import streamlit as st

st.header("Conclusion")

st.write("""<div style="text-align: justify">
Ce projet a permis de comparer différentes approches de classification pour la détection de crises d’épilepsie à partir de signaux audio dans un contexte de données déséquilibrées. 
   
Après avoir testé des méthodes classiques de machine learning, des modèles pré-entraînés (Wav2Vec2), et des réseaux neuronaux convolutifs (CNN), ce sont les CNN appliqués à des segments de 2 secondes qui ont offert le meilleur compromis entre performances (F1-score = 0.79), robustesse au déséquilibre des classes, et efficacité computationnelle. 
         
Cette solution constitue aujourd’hui la base retenue pour la suite du projet.
</div>""", unsafe_allow_html=True)

st.title('Critiques et perspectives')

# --- Difficultés rencontrées ---
st.subheader(':orange[Difficultés rencontrées]')

with st.expander("🔒 Verrou scientifique principal"):
    st.caption("Le principal défi a été la gestion du signal audio, très sensible aux bruits de fond et à la variabilité des lieux d’enregistrement (environnement hospitalier). Cela a complexifié l’équilibrage des classes et limité la généralisabilité des modèles.")

with st.expander("🔮 Prévisionnel et organisation"):
    st.caption("Certaines tâches ont été plus chronophages que prévu :")
    st.markdown("""
    - L’extraction de caractéristiques audio a nécessité de nombreux tests pour identifier les meilleures représentations ;
    - La configuration de Docker a posé des problèmes de compatibilité avec les bibliothèques audio et deep learning ;
    - L’exploration de CuDF a été abandonnée en raison d’incompatibilités ;
    - LazyPredict, utilisé pour un repérage initial de modèles, a finalement été écarté au profit d’approches plus ciblées.
    """)

with st.expander("📊 Données disponibles"):
    st.caption("Aucune nouvelle source externe de données audio n’a pu être intégrée.")
    st.caption("Le fort déséquilibre entre les classes a nécessité des techniques d’undersampling, réduisant la diversité des segments d’apprentissage.")

with st.expander("🤓 Compétences mobilisées"):
    st.caption("Le projet a nécessité d’anticiper sur le programme de formation, notamment en deep learning audio (modélisation CNN, représentation fréquentielle, gestion de classes déséquilibrées).")

with st.expander("💻 Ressources informatiques"):
    st.caption("Malgré l’usage de GPU, l’entraînement des modèles sur de gros volumes a été limité par la mémoire et les temps de traitement. Des ajustements (batch size, pipeline, prétraitement) ont été indispensables.")

# --- Perspectives ---
st.subheader(':green[Perspectives et pistes d\'amélioration]')

st.markdown("""<div style="text-align: justify"> Les CNN appliqués à des segments de 2 secondes ont montré de bons résultats pour la détection de crises à partir du signal vocal. Néanmoins, plusieurs axes d'amélioration sont à envisager pour renforcer la robustesse, la généralisabilité et l'applicabilité du modèle.</div>""", unsafe_allow_html=True)
st.markdown("")

with st.expander("📈 Diversification des données"):
    st.caption("Inclure des enregistrements issus de contextes variés (cliniques, linguistiques, acoustiques) permettrait de renforcer la robustesse et la transférabilité du modèle.")

with st.expander("⏱️ Affinage temporel"):
    st.caption("Explorer des fenêtres glissantes, adaptatives ou des modèles à mémoire longue (LSTM, Transformers) pour mieux capturer la dynamique temporelle des crises.")

with st.expander("⚖️ Rééquilibrage des classes"):
    st.caption("Tester des alternatives comme le focal loss, le suréchantillonnage synthétique (ex : SMOTE audio), ou des approches probabilistes pour mieux gérer les classes minoritaires.")

with st.expander("🧠 Optimisation des modèles"):
    st.caption("Explorer d'autres architectures efficaces pour les signaux audio et optimiser les fonctions de perte en intégrant des métriques centrées sur le rappel (rappel > précision pour les crises).")

with st.expander("👩🏻‍⚕️ Évaluation en conditions réalistes"):
    st.caption("Valider le modèle sur d’autres patients ou corpus indépendants, et tester un pipeline temps réel pour une application embarquée.")

with st.expander("🏥 Vers un usage clinique et multimodal"):
    st.caption("Combiner le signal audio à d'autres modalités (vidéo, ECG, accéléromètre) renforcerait la fiabilité. Le développement de modèles explicables favoriserait leur adoption en clinique.")

st.subheader('Remerciements')

with st.expander("🙏🏼 :rainbow[Remerciements]"):
    st.markdown(""" À l'issue de notre projet, nous souhaitons exprimer notre gratitude envers les personnes qui ont soutenu notre travail. Leur contribution a été essentielle à la réalisation de cette étude.""")
    st.markdown("""Ainsi, nous tenons tout particulièrement à remercier chaleureusement :""")                
    st.markdown("""* 👨🏽‍⚕️ Dr Mario Chavez, à l'initiative de ce projet, pour sa généreuse fourniture des données anonymisées et annotées, indispensables à notre travail.""")
    st.markdown("""* 👨🏻‍⚕️ Dr Valerio Frazzini, qui a récolté, sélectionné et annoté les données, assurant ainsi leur qualité et leur pertinence pour notre étude.""")
    st.markdown("""* 👨🏻‍💻 Thomas Boehler, notre chef de cohorte et encadrant sur ce projet, pour sa guidance précieuse et son accompagnement lors de nos moments d'incertitude, en nous orientant vers les bonnes démarches.""")
    st.markdown("""* 👩🏽‍💻 Aïda, notre Program Manager, pour la gestion de la planification des réunions sur la plateforme DataScientest, facilitant ainsi le bon déroulement de notre formation.""")
    st.markdown("""Et enfin, un grand merci à l’ensemble de l’équipe de notre établissement de rattachement DataScientest.""")