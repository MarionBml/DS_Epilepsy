'''
Prédiction :
- glisser fichier audio
- choix du modèle
- classification de l'audio à travers le modèle

'''
import io
import streamlit as st
import utils.plots as plots
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
    uploaded_file = st.file_uploader(
        "Chargez votre fichier audio",
        type=".wav"
    )
else:
    uploaded_file = st.audio_input("Enregistrez votre audio.")
st.markdown("")

if bool(uploaded_file):
    # Loading models
    uploaded_bytes = uploaded_file.read()
    file_buffer = io.BytesIO(uploaded_bytes)
    file_buffer.seek(0)  # Toujours repositionner le curseur

    st.subheader("Visualisation de l'enregistrement")
    st.audio(file_buffer)
    file_buffer.seek(0)
    plots.plot_audio(file_buffer)
    file_buffer.seek(0)

    # Choix du modèle
    st.subheader("""Choix du modèle""")
    # duration = st.radio('Choisissez la longueur des tranches (en secondes):', [1, 2, 4])
    model_choice = st.selectbox('Choisissez un modèle', ["CNN", "Undersampling + Wav2Vec", "Wav2Vec + GradientBoosting"])

    if model_choice == "CNN":
        # CNN = tb.CNN()
        predictions = tb.CNN.predict(file_buffer)
        file_buffer.seek(0)

    elif model_choice == "Wav2Vec + GradientBoosting" :
        # wvc = tb.Wav2VecClassified()
        predictions = tb.Wav2VecClassified.predict(file_buffer)
        file_buffer.seek(0)

    else:
        # wvt = tb.Wav2VecTrained()
        predictions = tb.Wav2VecTrained.predict(file_buffer)
        file_buffer.seek(0)

    df = tb.transform(predictions)

    st.subheader("Représentation graphique du diagnostic")
    plots.plot_model(df, file_buffer)
    file_buffer.seek(0)
