'''
Description et justification preprocessing effectué

'''

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

@st.cache_data
def load_chart_model_performance_analysis():
    # Valeurs obtenues en faisant tourner le code"preprocessing_analysis.ipynb"
    dic = {"Isolation Forest 5%": [93.35, 95.45, 96.56],
        "Centroids": [15.81, 97.61, 5.15],
        "Default": [97.78, 11.60, 19.65]}
    df2 = pd.DataFrame(data=dic, index=['Precision', 'Recall', 'F1'])
    st.dataframe(df2)

    # Reset index to bring metrics as a column
    df2_melted = df2.transpose().reset_index().melt(id_vars='index', var_name='Metric', value_name='Score')

    # Create grouped bar plot
    fig = px.bar(
        df2_melted,
        x='Metric',
        y='Score',
        color='index',  # Different colors for Precision, Recall, F1
        barmode='group',  # Grouped bars
        title='Model Performance Comparison',
        labels={'index': 'Model', 'Score': 'Score (%)'},
        color_discrete_sequence=px.colors.qualitative.Safe
    )
    return fig

st.title('Preprocessing des données')
st.markdown("""<div style="text-align: justify"> Afin d'explorer la faisabilité de la détection automatique des crises à partir des signaux audio, 
            nous avons d'abord extrait des caractéristiques statistiques de nos enregistrements sonores 
            en vue de les classifier par des méthodes de machine learning traditionnelles.</div>""", unsafe_allow_html=True)


st.subheader("Prétraitement et extraction de caractéristiques")

st.markdown("""<div style="text-align: justify"> Les modules nécessaires ont été importés et les données ont été chargées 
            individuellement pour chaque patient. Les signaux audio ont été découpés en fenêtres de 1 seconde, 
            conformément aux pratiques observées dans la littérature, avec un chevauchement de 25 %. 
            Chaque segment a été labellisé comme contenant ou non une activité épileptique.</div>""", unsafe_allow_html=True)
st.markdown("")
st.markdown("""<div style="text-align: justify"> Une transformation dans le domaine fréquentiel a été réalisée 
            à l’aide d’une représentation en spectrogramme de type mel scale, permettant d’estimer la puissance du signal 
            par bande de fréquence. Afin d’homogénéiser les amplitudes, une échelle logarithmique a été appliquée. 
            Nous avons retenu 80% de la fréquence de Fourier maximale théorique, ce qui permet de conserver les harmoniques 
            significatives tout en minimisant les artéfacts liés au sur-échantillonnage.</div>""", unsafe_allow_html=True)
st.markdown("")
st.markdown("""<div style="text-align: justify"> Nous avons également extrait des caractéristiques temporelles telles 
            que la moyenne, l’écart-type, et un décalage temporel de 3 secondes pour intégrer une dynamique temporelle 
            de 4 secondes.</div>""", unsafe_allow_html=True)
st.markdown("")
st.image("images/4_windows.png","""Pour chaque fenêtre, une séquence de 4 secondes est constituée
en incluant la seconde actuelle (:violet[en violet]) et les trois secondes qui la précèdent (:blue[en bleu]).
Cette approche permet de capturer la dynamique temporelle des signaux en conservant un historique pertinent pour l’analyse,
tout en assurant une dissociation claire entre les séquences utilisées pour l’entraînement et celles destinées au test.""")

st.badge("Sélection des caractéristiques et premières classifications", color='blue')
st.markdown("""<div style="text-align: justify"> Un premier pipeline d’analyse a été mis en place : 
            une sélection des meilleures bandes fréquentielles a été effectuée par SelectKBest, 
            suivie d’une réduction de dimensionnalité par PCA, 
            avant l'entraînement d’un classificateur de type Gradient Boosting. 
            Cette première approche n’a toutefois pas produit de résultats satisfaisants, 
            tant en termes d’accuracy que de F1-score. </div>""", unsafe_allow_html=True)

st.markdown("")
st.image("images/4_logistic_regression.png")

st.badge("Amélioration du pipeline et comparaison de méthodes", color='blue')
st.markdown("""<div style="text-align: justify"> Pour rationaliser notre approche et améliorer la robustesse, 
            nous avons abandonné la sélection par KBest au profit d’une réduction unique via PCA. 
            Nous avons ensuite comparé plusieurs pipelines de classification :</div>""", unsafe_allow_html=True)
st.markdown("""* **PCA + GradientBoosting**""")
st.markdown("""* **PCA + Centroid-based classification + GradientBoosting**""")
st.markdown("""* **PCA + IsolationForest** (avec un ratio d’anomalies fixé à 5 %, 
            correspondant à la proportion des crises dans les données d'entraînement)""")
st.markdown("")

st.plotly_chart(load_chart_model_performance_analysis(), use_container_width=True)


st.markdown("""<div style="text-align: justify"> Les performances ont été évaluées en accuracy, recall et F1-score, 
            comme illustré dans la figure ci-dessus. Le pipeline utilisant Isolation Forest avec un seuil à 5 % 
            a montré des performances très supérieures, particulièrement en termes de F1-score, 
            par rapport aux autres méthodes. En revanche, les approches basées sur les centroïdes et GradientBoosting 
            n’ont pas permis de capturer efficacement la complexité des signaux.</div>""", unsafe_allow_html=True)
st.markdown("")
st.markdown("""<div style="text-align: justify"> L’algorithme Isolation Forest a été utilisé dans une perspective 
            non supervisée, en s’appuyant sur des descripteurs simples du signal audio, notamment la moyenne et l’écart-type glissants. 
            Son principe repose sur l’identification d’échantillons "anormaux", c’est-à-dire rares ou atypiques par rapport 
            à la distribution globale, ce qui en fait une méthode potentiellement adaptée à la détection d’événements rares 
            comme les crises épileptiques.</div>""", unsafe_allow_html=True)
st.markdown("")
st.markdown("""<div style="text-align: justify">Dans notre cas, l’algorithme a été informé indirectement de la proportion 
            réelle de crises dans le jeu de données d'entraînement (fixée à 5 %), ce qui constitue une forme de biais 
            supervisé dans un cadre théoriquement non supervisé. Ce paramétrage a favorisé la détection d’épisodes 
            rares correspondant aux crises, permettant ainsi d'obtenir de bons résultats en F1-score sur le jeu de test.</div>""", unsafe_allow_html=True)
st.markdown("")
st.markdown("""<div style="text-align: justify"> Cependant, cette performance ne garantit pas une capacité de généralisation 
            dans un contexte réel, où la proportion de crises peut varier fortement, voire être inconnue. De plus, 
            la nature semi-supervisée de notre utilisation de l’Isolation Forest remet en question son caractère pleinement 
            non supervisé, et peut entraîner un surapprentissage sur la structure artificielle du jeu d'entraînement.</div>""", unsafe_allow_html=True)
st.markdown("")
st.markdown("""<div style="text-align: justify"> En résumé, bien que l’approche par Isolation Forest ait montré des performances prometteuses,
             notamment en termes de rappel (recall) des événements rares, ces résultats doivent être interprétés avec prudence. 
            Ils illustrent le potentiel de détection basé sur des dynamiques statistiques simples du signal audio, 
            mais soulignent également la nécessité de valider ces méthodes sur des données indépendantes et dans des conditions 
            réalistes, sans connaissance préalable du ratio crise/non-crise.</div>""", unsafe_allow_html=True)
st.markdown("")

st.subheader("Limites des techniques de machine learning")
st.markdown("""<div style="text-align: justify"> Malgré l’exploration de plusieurs configurations de prétraitement, 
            les approches classiques de machine learning se sont avérées inadaptées à la détection fiable des crises 
            sur signal audio. Nos essais confirment que ces méthodes restent limitées face à la complexité temporelle, 
            spectrale et contextuelle des enregistrements.</div>""", unsafe_allow_html=True)
st.markdown("")
st.markdown("""<div style="text-align: justify"> Nos résultats montrent en effet une forte sensibilité de ces méthodes 
            à la configuration des données et un manque de robustesse dans la détection de classes déséquilibrées. 
            Par exemple, malgré plusieurs combinaisons de prétraitements (PCA seule, PCA + Kbest, PCA + sélection par centroïdes), 
            aucune des configurations testées avec le Gradient Boosting n’a permis d’atteindre des scores F1 satisfaisants, 
            en particulier dans notre cas avec des données déséquilibrées. En revanche, l’approche Isolation Forest 
            avec un ratio de contamination ajusté à 5 %, bien que non supervisée, a montré des résultats plus stables, 
            en particulier en termes de précision et de F1-score. Cependant, cette performance ne garantit pas une capacité 
            de généralisation dans un contexte réel.</div>""", unsafe_allow_html=True)
st.markdown("")
st.markdown("""<div style="text-align: justify"> Ces résultats illustrent trois défis majeurs qui limitent l’efficacité 
            des méthodes classiques dans notre cas :</div>""", unsafe_allow_html=True)
st.markdown("")
with st.expander("⛔ Capacité de modélisation restreinte"):
    st.caption("""Les modèles comme Gradient Boosting reposent sur des caractéristiques extraites manuellement 
               (features d’énergie fréquentielle, moyenne, écart-type) et ont du mal à capturer la complexité temporelle 
               et spectrale des signaux audio liés aux crises, notamment lorsqu’ils présentent des variations subtiles 
               ou spécifiques à un patient.""")
with st.expander("⚖️ Difficultés à gérer les déséquilibres de classe"):
    st.caption("""La rareté relative des événements d’intérêt par rapport aux segments non épileptiques biaise 
               l’apprentissage des classifieurs supervisés. Malgré des stratégies comme l’ajustement des ratios 
               ou la détection par centroïdes, les performances en rappel ou en F1-score restent faibles pour certaines approches.""")
with st.expander("🔊 Sensibilité au bruit et à la variabilité"):
    st.caption(""" Les enregistrements contiennent souvent du bruit de fond (voix, mouvements), 
               rendant la séparation entre signal épileptique et non épileptique difficile pour des modèles 
               qui ne bénéficient pas d’une représentation hiérarchique des données.""")
st.markdown("")
st.markdown("""<div style="text-align: justify"> Par ailleurs, les approches traditionnelles nécessitent souvent 
            des ajustements manuels (feature engineering, équilibrage des classes) qui deviennent rapidement inadaptés 
            à l'échelle lorsque le volume de données augmente ou que la variabilité inter-patient s'accroît.</div>""", unsafe_allow_html=True)
st.markdown("")
st.markdown("""<div style="text-align: justify"> En somme, si l’Isolation Forest a pu offrir un aperçu des bénéfices 
            d’approches non conventionnelles dans ce contexte, elle reste limitée par sa dépendance à un réglage 
            fin du taux d’anomalie et à des caractéristiques simples. C’est pourquoi un changement de paradigme s’impose, 
            en s’orientant vers des architectures de deep learning, capables de s’abstraire des contraintes du feature 
            engineering et de modéliser la complexité acoustique réelle des crises épileptiques.</div>""", unsafe_allow_html=True)
