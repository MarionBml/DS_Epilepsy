'''
Prédiction :
- glisser fichier audio 
- choix du modèle 
- classification de l'audio à travers le modèle

'''

import pandas as pd
import streamlit as st
import utils.plots as plots
from scipy.io import wavfile
import plotly.express as px
import utils.toolbox as tb
import matplotlib.pyplot as plt


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
    labels = st.toggle("Labels disponibles", value=False)
    if labels == True : 
        uploaded_labels = st.file_uploader("Chargez vos étiquettes", type=".xlsx")
        diag = pd.read_excel(uploaded_labels, index_col=0)

else : 
    uploaded_file = st.audio_input("Enregistrez votre audio.")
st.markdown("")

if uploaded_file != None :
    st.subheader("Visualisation de l'enregistrement")
    st.audio(uploaded_file)
    plots.plot_audio(uploaded_file)

    # Choix du modèle
    st.subheader("""Choix du modèle""")
    #duration = st.radio('Choisissez la longueur des tranches (en secondes):', [1, 2, 4])
    model_choice = st.selectbox('Choisissez un modèle', ["Undersampling + Wav2Vec","Wav2Vec + GradientBoosting", "CNN"])

    if model_choice == "CNN" :
        cnn  = tb.CNN()
        array = cnn.load_audio_cnn(uploaded_file)
        predictions = cnn.predict(uploaded_file)

    elif model_choice == "Wav2Vec + GradientBoosting" :
        wvc= tb.Wav2VecClassified()
        predictions = wvc.predict(uploaded_file)

    else : 
        wvt = tb.Wav2VecTrained()
        predictions = wvt.predict(uploaded_file)

    df_pred = pd.DataFrame(predictions)
    df_pred.columns = ["Diagnostic"]
    df_pred['Diagnostic'] = df_pred['Diagnostic'].replace([0,1], ["Non-crise", "Crise"])
    
    if labels == True :
        df_pred = pd.concat([df_pred, diag], axis=1)
    st.dataframe(df_pred)
        #df_pred est un dataframe formé d'une seule colonne qui correspond au diagnostic (1: crise, 0: non-crise) pour chaque bande

    st.subheader("Représentation graphique")
    plots.plot_model(uploaded_file)
