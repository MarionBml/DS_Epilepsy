'''
Présentation des données (volumétrie, architecture, etc.)

'''
import streamlit as st

st.title('Données')
st.subheader('Présentation des données')

with st.expander("Contexte"):
    st.markdown("""
    Ce projet de recherche se base sur des données collectées dans le cadre d'une étude menée à l'Hôpital Universitaire Pitié-Salpêtrière à Paris. Les patients épileptiques sélectionnés pour cette étude sont des cas pharmaco-résistants, candidats à une chirurgie. Ils subissent une implantation d'électrodes intracrâniennes dans le but de déterminer le foyer à l'origine des crises. La phase d’observation dure deux à trois semaines et est accompagnée d’une surveillance vidéo-encéphalographique (VEEG), offrant une documentation précieuse de l'activité cérébrale pendant les crises. Ces données ont été fournies par l'hôpital pour cette recherche.
    """, unsafe_allow_html=True)
    st.markdown("")

with st.expander("Caractéristiques techniques"):
    st.markdown("""
    Les données utilisées dans ce projet proviennent des enregistrements audio extraits des vidéos capturées pendant la surveillance VEEG. Les vidéos ont été prises avec une caméra réseau AXIS M5525–E PTZ et un microphone analogique AXIS T8351 Mk II, conçu pour capter des sons à faible bruit sur toutes les directions. Ces enregistrements incluent des périodes de silence et des bruits de fond, tels que des discussions externes, ainsi que des périodes ictales clairement annotées par un neurologue. 

    Pour cette étude, les fichiers audio, au format MP4 avec un taux d'échantillonnage de 32 kHz, ont été extraits des vidéos et traités à l'aide de l'Audio Toolbox™ de MATLAB R2023b. Le traitement des données a été effectué par le Dr Mario Chavez pour garantir l’anonymat des patients.
    """, unsafe_allow_html=True)
    st.markdown("")
    st.image("images/2_microphones.png", "a) Caméra AXIS M5525-E PTZ et b) Microphone AXIS T8351 Mk II")

st.subheader('Variables pertinentes et cible')
st.markdown("""
Pour détecter les crises épileptiques à partir des données audio, plusieurs variables sont cruciales :
- **Vocalisations** : Cris et pleurs pouvant indiquer une crise.
- **Automatismes vocaux** : Paroles incohérentes ou répétitives comme signes d’une crise.
- **Altération de la parole** : Modifications de la parole liées à la crise.
- **Modifications respiratoires** : Halètements et apnées associés à une crise.
- **Bruits moteurs** : Sons d'impact et de frottement liés aux mouvements involontaires.
- **Interactions avec l’environnement** : Bruits d’objets ou mouvements involontaires pendant une crise.

La variable cible de notre analyse est la **présence ou l'absence de crise épileptique**, détectée à partir du signal audio.
""")

st.subheader('Particularités des données')
st.markdown("""
Notre jeu de données présente plusieurs spécificités qui influencent l’analyse :
- **Variabilité des sons** : Les sons varient selon le type de crise et les patients, rendant la classification complexe.
- **Bruit ambiant** : Le bruit de fond peut interférer avec la détection des crises.
- **Exploitation des caractéristiques audio** : Des caractéristiques comme par exemple les **MFCC** ou **l'entropie spectrale** doivent être extraites pour l'apprentissage automatique. 

Ces caractéristiques guideront nos efforts pour optimiser la performance du modèle face aux défis posés par la variabilité et le bruit ambiant.
""")

st.subheader('Limites et défis')
st.markdown("""
Nous faisons face à plusieurs défis pouvant affecter la performance des modèles :
- **Généralisation des modèles** : Les différences entre les patients rendent la généralisation difficile.
- **Bruit de fond** : Des sons non liés aux crises, comme des conversations, peuvent interférer avec la détection.
- **Quantité de données** : Une crise par patient seulement et un jeu de données déséquilibré.
- **Biais dans les données** : Les données issues d’un environnement clinique peuvent ne pas être représentatives des conditions réelles.

Ces limitations doivent être prises en compte pour améliorer la précision de la détection des crises dans des contextes variés.
""")
