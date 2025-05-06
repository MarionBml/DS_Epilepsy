'''
Prédiction :
- glisser fichier audio 
- choix du modèle 
- classification de l'audio à travers le modèle

'''
from io import StringIO
import os
import re
import streamlit as st
import numpy as np
from scipy.io import wavfile

import utils.toolbox as tb


st.title('Prédiction')
st.write("""
Démonstration de prédiction à l'aide d'un des modèles mis en avant par notre équipe.
""")

# Glisser fichier audio
st.subheader("""Choix du fichier audio""")
st.write("""
Enregistrez ou importez votre fichier audio afin d'estimer quels moments représentent des moments de crise.
""")
st.markdown("")

uploaded_file = None
options = ["Importer un fichier", "Enregistrer du son"]
selection = st.segmented_control("Audio à analyser :", options, selection_mode="single")
st.markdown("")
if selection == "Importer un fichier":
    uploaded_file = st.file_uploader("Chargez votre fichier audio", type=".wav")
else : 
    uploaded_file = st.audio_input("Enregistrez votre audio.")
st.markdown("")
st.audio(uploaded_file)

# Choix du modèle
st.subheader("""Choix du modèle""")
#duration = st.radio('Choisissez la longueur des tranches (en secondes):', [1, 2, 4])
model_choice = st.selectbox('Choisissez un modèle', ["Undersampling + Wav2Vec","Wav2Vec + GradientBoosting", "CNN"])

if uploaded_file != None :
    if model_choice == "CNN" :
        cnn  = tb.CNN()
        df_audio_files = cnn.load_audio_cnn(df_audio_files=uploaded_file)
    
        model = cnn.load_model()

        predictions = model.predict(df_audio_files)
        y_predicted = np.argmax(predictions, axis=1)

        df_audio_files['predicted label'] = y_predicted

        st.dataframe(df_audio_files.head())
