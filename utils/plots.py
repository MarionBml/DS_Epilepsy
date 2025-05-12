import librosa
import streamlit as st
import plotly.graph_objs as go
from pydub import AudioSegment
import numpy as np

@st.cache_data
def plot_trace(samples, sr, df):
    # -------- Forme d'onde --------
    duration = len(samples) / sr
    time = np.linspace(0, duration, num=len(samples))
    fig_wave = go.Figure()
    # Trace audio
    fig_wave.add_trace(
        go.Scatter(
            x=time,
            y=samples,
            mode='lines',
        )
    )
    # Ajouter des zones de crise
    for _, row in df.iterrows():
        if row['diagnostic'] == "Crise":
            fig_wave.add_vrect(
                x0=row['start'],
                x1=row['end'],
                fillcolor='red',
                opacity=0.3,
                line_width=0,
                annotation_text='Crise',
                annotation_position='top left'
            )
    fig_wave.update_layout(
        title="Tracé audio avec diagnostic",
        xaxis_title="Temps (s)",
        yaxis_title="Amplitude",
        showlegend=False
    )
    return st.plotly_chart(fig_wave)


def plot_hist(samples):
    # -------- Histogramme --------
    fig = go.Figure(
        data=[
            go.Histogram(
                x=samples,
                nbinsx=100,
                marker_color='indianred',
            )
        ],
    )
    fig.update_layout(
        title="Distribution des amplitudes audio",
        xaxis_title="Amplitude (normalisée)",
        yaxis_title="Nombre d’occurrences",
        bargap=0.05
    )
    return fig


def plot_spec(samples, sr):
    # -------- Spectogramme --------
    # Calcul du Mel-spectrogramme
    mel_spec = librosa.feature.melspectrogram(
        y=samples,
        sr=sr,
        n_fft=2048,
        hop_length=512,
        n_mels=40,
    )
    mel_spec_db = librosa.power_to_db(mel_spec, ref=np.max)

    # Axe du temps et axe des fréquences mel
    times = librosa.frames_to_time(
        np.arange(
            mel_spec_db.shape[1]
        ),
        sr=sr,
        hop_length=512
    )
    mel_frequencies = librosa.mel_frequencies(n_mels=40)

    # Création de la heatmap avec Plotly
    fig = go.Figure(
        data=go.Heatmap(
            z=mel_spec_db,
            x=times,
            y=mel_frequencies,
            colorscale='Viridis',
            colorbar=dict(title="dB")
        )
    )
    fig.update_layout(
        title="Mel-Spectrogramme",
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


@st.cache_data
def plot_audio(file):
    samples, sr = transform_audio(file)
    col1, col2 = st.columns(2)
    col1.plotly_chart(plot_spec(samples, sr), use_container_width=True)
    col2.plotly_chart(plot_hist(samples), use_container_width=True)
    return None


@st.cache_data()
def plot_model(df, file=None):
    samples, sr = transform_audio(file)
    plot_colored_waveform(samples, sr, df)
    return None


def plot_colored_waveform(y, sr, predictions, duration=2):
    fig = go.Figure()
    samples_per_segment = int(sr * duration)

    for i, label in enumerate(predictions['diagnostic']):
        start_sample = i * samples_per_segment
        end_sample = start_sample + samples_per_segment
        segment_y = y[start_sample:end_sample]
        segment_x = np.linspace(
            start_sample / sr,
            end_sample / sr,
            num=len(segment_y)
        )

        color = '#CD5C5C' if label == "Crise" else '#D6E3F8'

        fig.add_trace(
            go.Scatter(
                x=segment_x,
                y=segment_y,
                mode='lines',
                line=dict(color=color),
                name=f'Segment {i} - {"Crise" if label == "Crise" else "Non-Crise"}',
                showlegend=True
            )
        )

    fig.update_layout(
        title="Trace audio colorée selon la prédiction",
        xaxis_title="Temps (s)",
        yaxis_title="Amplitude"
    )

    return st.plotly_chart(fig)
