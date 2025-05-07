import librosa
import streamlit as st
import plotly.graph_objs as go
from pydub import AudioSegment
import numpy as np

def plot_trace(samples, sr): # -------- Forme d'onde --------
    
    duration = len(samples) / sr
    time = np.linspace(0, duration, num=len(samples))

    fig_wave = go.Figure()
    fig_wave.add_trace(go.Scatter(x=time, y=samples, mode='lines'))
    fig_wave.update_layout(title="Forme d'onde audio", xaxis_title="Temps (s)", yaxis_title="Amplitude")
    st.plotly_chart(fig_wave)

def plot_hist(samples):# -------- Histogramme --------
    
    fig = go.Figure(data=[
        go.Histogram(x=samples, nbinsx=100, marker_color='indianred')
    ])
    
    fig.update_layout(
        title="Distribution des amplitudes audio",
        xaxis_title="Amplitude (normalisée)",
        yaxis_title="Nombre d’occurrences",
        bargap=0.05
    )

    return fig

def plot_spec(samples, sr):# -------- Spectogramme --------

    # Calcul du Mel-spectrogramme
    mel_spec = librosa.feature.melspectrogram(y=samples, sr=sr, n_fft=2048, hop_length=512, n_mels=128)
    mel_spec_db = librosa.power_to_db(mel_spec, ref=np.max)

    # Axe du temps et axe des fréquences mel
    times = librosa.frames_to_time(np.arange(mel_spec_db.shape[1]), sr=sr, hop_length=512)
    mel_frequencies = librosa.mel_frequencies(n_mels=128)

    # Création de la heatmap avec Plotly
    fig = go.Figure(data=go.Heatmap(
        z=mel_spec_db,
        x=times,
        y=mel_frequencies,
        colorscale='Viridis',
        colorbar=dict(title="dB")
    ))

    fig.update_layout(
        title="Mel-Spectrogramme (interactif)",
        xaxis_title="Temps (s)",
        yaxis_title="Fréquence (Hz)",
        yaxis_type="log"
    )

    return fig

def transform_audio(file):
    # Charger l'audio avec pydub
    audio = AudioSegment.from_file(file, format="wav")
    
    # Convertir en tableau numpy
    samples = np.array(audio.get_array_of_samples()).astype(np.float32)
    
    # Gérer les fichiers stéréo
    if audio.channels == 2:
        samples = samples.reshape((-1, 2))
        samples = samples[:, 0]  # Ne garder qu'un canal

    # Normalisation entre -1 et 1
    samples /= np.iinfo(np.int16).max
    sr = audio.frame_rate
    return samples, sr

def plot_audio(file):
    samples, sr = transform_audio(file)

    col1, col2 = st.columns(2)
    col1.plotly_chart(plot_spec(samples, sr), use_container_width=True)
    col2.plotly_chart(plot_hist(samples), use_container_width=True)

    return None
        
def plot_model(file:None, labels:None):
    samples, sr = transform_audio(file)
    plot_trace(samples, sr)
    
    return None
