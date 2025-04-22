'''
Prédiction :
- glisser fichier audio 
- choix du modèle 
- classification de l'audio à travers le modèle

'''
import streamlit as st

st.title('Prédiction')
st.write("""
Démonstration de prédiction à l'aide d'un des modèles mis en avant par notre équipe.
""")

# Glisser fichier audio
st.subheader("""Choix du fichier audio""")
st.write("""
Importez votre fichier audio afin d'estimer quels moments représentent des moments de crise
""")

uploaded_file = st.file_uploader("Chargez votre fichier audio", type=".wav")

# Choix du modèle
st.subheader("""Choix du modèle""")
duration = st.radio('Choisissez la longueur des tranches (en secondes):', [1, 2, 10])
modele = st.selectbox('Choisissez un modèle', ["Undersampling + Wav2Vec","Wav2Vec + GradientBoosting", "CNN"])

# Classification de l'audio à travers le modèle

# Représentation graphique du résultat 
