import streamlit as st

st.title('Classification du problème')

st.markdown("""<div style="text-align: justify">
Le projet s'inscrit dans une démarche de <strong>classification binaire</strong> visant à distinguer deux états cérébraux : "crise" et "non-crise". Ces classes correspondent à la présence ou à l'absence d'une activité épileptique détectée à partir de données audio dérivées d’enregistrements Vidéo-EEG. L'objectif est de classifier chaque segment audio en fonction de la survenue d’une crise, à l’aide de caractéristiques temporelles et spectrales extraites des signaux.
</div>""", unsafe_allow_html=True)
st.markdown("")

st.markdown("""<div style="text-align: justify">
Sur le plan statistique, cette tâche repose sur l’entraînement d’un modèle de classification capable de distinguer deux catégories distinctes. Le modèle apprend à reconnaître les schémas caractéristiques associés aux crises, afin de prédire correctement l’étiquette des nouveaux segments selon les motifs appris.
</div>""", unsafe_allow_html=True)
st.markdown("")

st.markdown("""<div style="text-align: justify">
Ce projet mobilise également les principes de <strong>détection d’anomalies</strong>, les crises épileptiques étant des événements rares et atypiques par rapport à l’activité normale du cerveau. Contrairement à la classification classique nécessitant des exemples équilibrés des deux classes, la détection d’anomalies consiste souvent à entraîner le modèle uniquement sur des données "normales", de sorte qu’il puisse repérer toute déviation significative indicative d’une crise.
</div>""", unsafe_allow_html=True)
st.markdown("")

st.markdown("""<div style="text-align: justify">
Cette approche permet une détection plus fine d’événements critiques dans des ensembles de données fortement déséquilibrés, comme c’est souvent le cas dans les enregistrements vidéo-EEG où les crises sont peu fréquentes. Elle est donc particulièrement adaptée au contexte médical, où l’identification d’événements rares mais cliniquement significatifs est primordiale.
</div>""", unsafe_allow_html=True)
st.markdown("")

st.subheader('Métriques et outils')

st.markdown("""<div style="text-align: justify">
Pour évaluer les performances des modèles, plusieurs métriques de classification binaire sont utilisées :
</div>""", unsafe_allow_html=True)
st.markdown("")

with st.expander("Précision (Accuracy)"):
    st.caption("""Proportion globale d’exemples correctement classés. Elle peut toutefois être trompeuse dans des situations de déséquilibre des classes.""")

with st.expander("Précision (Precision) et Rappel (Recall)"):
    st.caption("""Essentielles en contexte médical. La précision indique la proportion de crises correctement identifiées parmi toutes les prédictions positives, tandis que le rappel mesure la capacité du modèle à détecter toutes les crises réellement présentes.""")

with st.expander("F1-Score"):
    st.caption("""Moyenne harmonique entre la précision et le rappel, offrant une mesure équilibrée, particulièrement utile en cas de classes déséquilibrées.""")

st.markdown("""<div style="text-align: justify">

            
D’autres outils permettent d’analyser plus finement les performances :
</div>""", unsafe_allow_html=True)

with st.expander("Matrice de confusion"):
    st.caption("""Tableau synthétique des prédictions, indiquant le nombre de vrais positifs, faux positifs, vrais négatifs et faux négatifs.""")

with st.expander("AUC-ROC"):
    st.caption("""Mesure de la capacité du modèle à discriminer les classes. Un AUC proche de 1 indique une excellente séparation entre les états "crise" et "non-crise".""")

with st.expander("Courbe de précision-rappel"):
    st.caption("""Particulièrement utile lorsque la classe minoritaire est la plus importante à détecter. Elle visualise le compromis entre précision et rappel selon différents seuils.""")

st.markdown("""<div style="text-align: justify">
Ces métriques permettent une évaluation rigoureuse de la capacité du modèle à détecter efficacement les crises épileptiques à partir des signaux audio issus des EEG.
</div>""", unsafe_allow_html=True)