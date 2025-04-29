'''
Prédiction :
- glisser fichier audio 
- choix du modèle 
- classification de l'audio à travers le modèle

'''
import os
import re
import streamlit as st
import numpy as np
from scipy.io import wavfile

#from utils.cnn_package import CNN
#from utils.core_functions import plot


st.title('Prédiction')
st.write("""
Démonstration de prédiction à l'aide d'un des modèles mis en avant par notre équipe.
""")

# Glisser fichier audio
st.subheader("""Choix du fichier audio""")
st.write("""
Importez votre fichier audio afin d'estimer quels moments représentent des moments de crise.
""")

uploaded_file = st.file_uploader("Chargez votre fichier audio", type=".wav")
# ajouter component pour laisser à l'utilisateurice la possibilité d'enregistrer un audio 
# idée : https://github.com/stefanrmmr/streamlit-audio-recorder

# Choix du modèle
st.subheader("""Choix du modèle""")
duration = st.radio('Choisissez la longueur des tranches (en secondes):', [1, 2, 4])
modele = st.selectbox('Choisissez un modèle', ["Undersampling + Wav2Vec","Wav2Vec + GradientBoosting", "CNN"])

# Classification de l'audio à travers le modèle
#if modele == "CNN":
#    cnn = CNN()
#    df_audio_files = cnn.load_audio_files(patient=PATIENT)
#    X, y = cnn.load_data_cnn(df_audio_files=df_audio_files)
#    model = CNN.load_pickle_model(model_file_path=os.path.join(ROOT, 'results', 'keras', f'wav2vec2_cnn_{duration}sec_model.h5'))

#elif modele == "Undersampling + Wav2Vec":
    #st.write("à remplir")

#else : 
    #st.write("à remplir")

#predictions = model.predict(X)
#y_predicted = np.argmax(predictions, axis=1)

#df_audio_files['true label'] = y
#df_audio_files['predicted label'] = y_predicted

#st.table(df_audio_files.iloc[0:10]) # Show first lines of the data

# Représentation graphique du résultat : à convertir sous format plus adapté à streamlit, par ex plotly

