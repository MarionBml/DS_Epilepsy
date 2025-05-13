
import librosa
import numpy as np
import pandas as pd
import os
import io
import pickle
import torch
from joblib import load
import streamlit as st
from datetime import datetime
from keras.models import load_model
from tensorflow.keras import backend as K
# from transformers import (
#     AutoModelForAudioClassification,
#     AutoProcessor,
#     Wav2Vec2ForCTC,
# )


ROOT = '.'
TEMP = 'temp'
SAMPLING_RATE = 16000
DURATION = 2  # en secondes


if not os.path.exists(os.path.join(ROOT, TEMP)):
    os.mkdir(os.path.join(ROOT, TEMP))


def write_log(log: str):
    formatted_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f'{formatted_datetime} - {log} ...')
    if not os.path.exists(os.path.join(ROOT, 'logs')):
        os.mkdir(os.path.join(ROOT, 'logs'))
    with open(os.path.join(ROOT, 'logs', 'output.log'), 'a') as f:
        f.write(f'{formatted_datetime} - {log} ...')
        f.write('\n')


def macro_f1_score(y_true, y_pred):
    with open('./logs.txt', 'a+') as f:
        f.write(f'y_true {type(y_true)} {y_true}\n')
        f.write(f'y_pred {type(y_pred)} {y_pred}\n')
    # Round predictions to 0 or 1 for binary classification
    y_pred = K.round(y_pred)

    # Initialize variables to accumulate the F1 score for each class
    f1_scores = []

    # Iterate over all classes (assuming y_true and y_pred are one-hot encoded)
    for i in range(y_true.shape[1]):  # for each class
        # Get true positives, false positives, and false negatives for class i
        true_positives = K.sum(K.cast(K.equal(y_true[:, i], 1) & K.equal(y_pred[:, i], 1), dtype='float32'))
        false_positives = K.sum(K.cast(K.equal(y_true[:, i], 0) & K.equal(y_pred[:, i], 1), dtype='float32'))
        false_negatives = K.sum(K.cast(K.equal(y_true[:, i], 1) & K.equal(y_pred[:, i], 0), dtype='float32'))

        # Calculate precision and recall for class i
        precision = true_positives / (true_positives + false_positives + K.epsilon())
        recall = true_positives / (true_positives + false_negatives + K.epsilon())

        # Calculate F1 score for class i
        f1 = 2 * (precision * recall) / (precision + recall + K.epsilon())

        # Append the F1 score for this class
        f1_scores.append(f1)

    # Calculate and return the macro F1 score (average of all class F1 scores)
    return K.mean(K.stack(f1_scores))


# def load_audio_raw(file):
#     if file.type != 'audio/wav':
#         raise Exception('The provided file is not a wav file.')

#     write_log('INFO: Loading the file')

#     if hasattr(file, "read"):  # si c'est un fichier en mémoire (Streamlit)
#         file_content = file.read()
#         file = io.BytesIO(file_content)
#         file.seek(0)  # Rewind for librosa

#     y, sr = librosa.load(file, sr=None)
#     #y, sr = librosa.load(filepath, sr=None)

#     if sr != SAMPLING_RATE:
#         y = librosa.resample(y=y, orig_sr=sr, target_sr=SAMPLING_RATE)
#         sr = SAMPLING_RATE

#     if len(y) / sr > DURATION:
#         write_log('INFO: Splitting the file in 2 second chunks')
#         recordings = []
#         for i in range(0, int(len(y) / sr / DURATION)):
#             # wav_file = f"output-{os.path.basename(filepath)[:-4]}-{i}.wav"
#             # wavfile.write(
#             #     os.path.join(
#             #         ROOT,
#             #         TEMP,
#             #         wav_file
#             #     ),
#             #     sr,
#             #     y[sr * i * DURATION: sr * (i + 1) * DURATION]
#             # )
#             recordings.append(y[sr * i * DURATION: sr * (i + 1) * DURATION])
#         return recordings, sr
#     return [], None

@st.cache_data()
def safe_load_audio(uploaded_file, sampling_rate=SAMPLING_RATE, duration=DURATION):
    """
    Charge un fichier audio Streamlit (.wav) de manière sécurisée.
    Découpe automatiquement en segments de `duration` secondes si nécessaire.

    Retourne : liste de segments (np.ndarray), sample rate
    """
    if uploaded_file is None:
        raise ValueError("Aucun fichier fourni.")

    # Lire le contenu du fichier et l'encapsuler dans un buffer
    file_content = uploaded_file.read()
    buffer = io.BytesIO(file_content)
    buffer.seek(0)

    # Charger avec librosa
    y, sr = librosa.load(buffer, sr=None)

    # Harmoniser le sampling rate si besoin
    if sr != sampling_rate:
        y = librosa.resample(
            y=y,
            orig_sr=sr,
            target_sr=sampling_rate
        )
        sr = sampling_rate

    # Découper en segments de `duration` secondes
    if len(y) / sr > duration:
        segments = []
        total_chunks = int(len(y) / sr / duration)
        for i in range(total_chunks):
            segments.append(y[sr * i * duration: sr * (i + 1) * duration])
        return segments, sr
    else:
        return [y], sr


class CNN():
    def __init__():
        # self.model = CNN.load_model()
        return None

    @st.cache_data()
    def load_audio_cnn(file):
        audios, sr = safe_load_audio(file)
        write_log('INFO: Loading recording data for CNN')
        features = []
        for audio in audios:
            mfccs = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=40)
            mfccs_scaled = np.mean(mfccs.T, axis=0)
            features.append(mfccs_scaled)
        # self.X = np.array(features)
        return np.array(features)

    @st.cache_resource
    def load_model():
        write_log('INFO: Loading the CNN Keras model')
        model = load_model(
            'models/wav2vec2_cnn_2sec_model.keras',
            custom_objects={
                'macro_f1_score': macro_f1_score
            },
        )
        return model

    @st.cache_data()
    def predict(file: None):
        # if not hasattr(self, 'X'):
        #     if file is None:
        #         raise Exception(
        #             'ERROR: Cannot load the audio as the file is not provided'
        #         )
        #     else:
        #         self.load_audio_cnn(file=file)

        # if not hasattr(self, 'model'):
        #     self.load_model()

        X = CNN.load_audio_cnn(file=file)
        model = CNN.load_model()
        write_log('INFO: Predicting using CNN')
        prediction_vectors = model.predict(X)
        predictions = np.argmax(prediction_vectors, axis=1)
        # self.predictions = predictions
        return predictions


class Wav2VecTrained():
    def __init__():
        # self.processor = Wav2VecTrained.load_processor()
        # self.model = Wav2VecTrained.load_model()
        return None

    @st.cache_resource
    def load_processor():
        from transformers import (
            AutoProcessor,
        )
        saved_model_path = 'models/wav2vec2_retrained_2sec'
        return AutoProcessor.from_pretrained(saved_model_path)

    @st.cache_data()
    def load_audio(file):
        audios, sr = safe_load_audio(file)
        write_log('INFO: Loading recording data for retrained Wav2Vec')
        processor = Wav2VecTrained.load_processor()
        inputs = processor(
            audios,
            sampling_rate=sr,
            return_tensors="pt",
            padding=True
        )
        input_values = inputs.input_values.squeeze()
        # Wav2VecTrained.input_values = input_values
        return input_values

    @st.cache_data()
    def predict(file:  None):
        # if not hasattr(self, 'model'):
        #     self.load_model()

        # if not hasattr(self, 'input_values'):
        #     if file is None:
        #         raise Exception(
        #             'ERROR: Cannot load the audio has the filepath is not provided'
        #         )
        #     else:
        #         self.load_audio(file=file)
        model = Wav2VecTrained.load_model()
        input_values = Wav2VecTrained.load_audio(file=file)
        write_log('INFO: Predicting using Wav2VecTrained')
        predictions = []
        with torch.no_grad():
            for batch in input_values.unsqueeze(0):
                input_values = batch.to("cuda" if torch.cuda.is_available() else "cpu")
                logits = model(input_values).logits
                predicted_ids = torch.argmax(logits, dim=-1)
                predictions += predicted_ids.cpu().tolist()
        # Wav2VecTrained.predictions = predictions
        return predictions

    @st.cache_resource
    def load_model():
        from transformers import (
            AutoModelForAudioClassification
        )
        write_log('INFO: Loading Wav2Vec retrained')
        saved_model_path = 'models/wav2vec2_retrained_2sec'
        model = AutoModelForAudioClassification.from_pretrained(saved_model_path)  # Load weights
        model.to("cuda" if torch.cuda.is_available() else "cpu")
        return model


class Wav2VecClassified():
    def __init__():
        # self.model = Wav2VecClassified.load_model()
        return None

    @st.cache_resource()
    def load_standard_Wav2Vec():
        from transformers import (
            AutoProcessor,
            Wav2Vec2ForCTC,
        )
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        processor = AutoProcessor.from_pretrained("facebook/wav2vec2-base-960h")
        model = Wav2Vec2ForCTC.from_pretrained(
            "facebook/wav2vec2-base-960h"
        ).to(device)
        with open('pca/wav2vec2_classifier_2sec_pca.pickle', 'rb') as f:
            pca = pickle.load(f)
        return processor, model, pca, device

    @st.cache_data()
    def load_audio(file):
        processor, model, pca, device = Wav2VecClassified.load_standard_Wav2Vec()
        audios, sr = safe_load_audio(file)
        features = []
        output_dict = {}
        for audio in audios:
            with torch.no_grad():
                input_values = processor(
                    audio,
                    sampling_rate=SAMPLING_RATE,
                    return_tensors="pt"
                ).input_values.squeeze().to(device)
                input_values = input_values.unsqueeze(0)
                logits = model(input_values=input_values).logits
                for i in range(logits.shape[0]):
                    for j, val in enumerate(logits[i].flatten().cpu()):
                        output_dict.setdefault(j, []).append(float(val))
                output_df = pd.DataFrame.from_dict(output_dict)
                # PCA was trained and pickle with column names
                output_df.rename(
                    columns={
                        c: str(c) for c in output_df.columns
                    },
                    inplace=True
                )
                features = pca.transform(output_df)
        # self.features = features
        return features

    @st.cache_resource
    def load_model():
        write_log('INFO: Loading Wav2Vec classifier')
        model = load("models/wav2vec2_classifier_2sec_model.joblib")
        return model

    @st.cache_data()
    def predict(file: str = None):
        # if not hasattr(self, 'model'):
        #     self.load_model()
        # if not hasattr(self, 'input_values'):
        #     if file is None:
        #         raise Exception('ERROR: Cannot load the audio has the filepath is not provided')
        #     else:
        #         self.load_audio(file=file)

        model = Wav2VecClassified.load_model()
        features = Wav2VecClassified.load_audio(file=file)
        write_log('INFO: Predicting using Wav2VecClassified')
        predictions = model.predict(features)
        # self.predictions = predictions
        return predictions


# if __name__ == '__main__':
#     filepath = r'./source/VID_261.wav'

#     cnn = CNN()
#     predictions = cnn.predict(filepath=filepath)

#     wv = Wav2VecTrained()
#     wv.predict(filepath=filepath)

#     wvc = Wav2VecClassified()
#     wvc.predict(file=file)

@st.cache_data()
def transform(predictions, labels=False, diag=None):
    df = pd.DataFrame(predictions)
    df.columns = ["diagnostic"]
    df['diagnostic'] = df['diagnostic'].replace(
        {
            0: "Non-crise",
            1: "Crise",
        }
    )
    df['start'] = [i * 2 for i in range(len(predictions))]
    df['end'] = [(i + 1) * 2 for i in range(len(predictions))]
    df = df.reindex(['start', 'end', 'diagnostic'], axis=1)

    if labels:
        df = pd.concat([df, diag], axis=1)

    return df
