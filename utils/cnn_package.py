import os
import librosa
import numpy as np
import pandas as pd
from keras.models import load_model
from scipy.io import wavfile

from utils.core_functions import write_log


# A adapter pour pouvoir utiliser sur un fichier loadé au lieu d'accéder aux paths
class CNN():
    def __init__(self, source_path: str = SOURCE_PATH, output_path: str = OUTPUT_PATH, duration: int = 2000, sampling_rate: int = 16000):
        self.source_path = source_path
        self.output_path = output_path
        self.duration = duration / 1000
        self.loaded_data_path = f'training_set_{self.duration}'
        self.sampling_rate = sampling_rate
    
    def update_path(self, x: str):
        return os.path.join(
                self.output_path,
                self.loaded_data_path,
                x,
            )

    def load_audio_files(self, patient: str):
        write_log(log=f'INFO: Loading data')
        df_patient = pd.read_excel(
                os.path.join(self.source_path, patient, f'PAT{patient}.xlsx')
            )

        write_log(f'INFO: Splitting video')
        indexes = df_patient.groupby(['folder', 'video'])['start_time'].count().index
        outputs = []

        if not os.path.exists(os.path.join(self.output_path, self.loaded_data_path)):
            os.mkdir(os.path.join(self.output_path, self.loaded_data_path))

        for folder, audio in indexes:
            # read the actual audio file
            sr, y = wavfile.read(
                os.path.join(
                    self.source_path,
                    str(folder),
                    f'{audio}.wav',
                ),
            )

            # Split the audio file in a list of 1 sec audio files and we associate a label based on the Excel input.
            # The outputs are a dataframe with the new list of 1 sec audio files and associated labels and the new list of audio files.
            for i in range(0,   int(len(y) / sr / self.duration)):
                wav_file = f"output-{folder}-{audio}-{i}.wav"
                wavfile.write(os.path.join(OUTPUT_PATH, self.loaded_data_path, wav_file), sr, y[int(sr * i * self.duration) : int(sr * (i + 1) * self.duration)])
                temp = df_patient[
                    (
                        df_patient['folder'].astype(str) == str(folder)
                    ) & (
                        df_patient['video'] == str(audio)
                    ) & (
                        df_patient['start_time'] <= i * self.duration
                    ) & (
                        df_patient['end_time'] >= i * self.duration
                    )
                ]
                if temp.shape[0] > 0:
                    outputs.append({'data':wav_file, 'label':temp['label'].values[0]})

        df = pd.DataFrame(outputs)
        df['data'] = df['data'].apply(self.update_path)
        return df
        
    def load_data_cnn(self, df_audio_files: pd.DataFrame):
        write_log('INFO: Loading the data for the CNN')
        features = []
        labels = []

        for idx, _ in df_audio_files.iterrows():
            audio, sample_rate = librosa.load(df_audio_files.loc[idx, 'data'], sr=self.sampling_rate)
            if sample_rate != self.sampling_rate:
                write_log('ERROR: Sampling rates mismatch')
                raise

            mfccs = librosa.feature.mfcc(y=audio, sr=self.sampling_rate, n_mfcc=40)
            mfccs_scaled = np.mean(mfccs.T, axis=0)

            features.append(mfccs_scaled)
            labels.append(df_audio_files.loc[idx, 'label'])

        y = np.where(np.array(labels) == 'seizure', 1, 0)
        return np.array(features), y

    def load_pickle_model(model_file_path: str, custom_objects: dict = None):
        write_log(f'INFO: Loading the model {os.path.basename(model_file_path)}')
        if not os.path.exists(model_file_path):
            write_log(f'ERROR: File path does not exist: {model_file_path}')
        return load_model(model_file_path, custom_objects=custom_objects)
