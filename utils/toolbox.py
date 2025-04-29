from datetime import datetime
import os
import librosa
import pandas as pd

# write_log function removed

def get_recordings(root: str, folder: str):
    """
    Return the list of wav files in a folder.
    """
    path = os.path.join(root, folder).replace('/', '\\')
    if os.path.exists(path):
        return [f for f in os.listdir(path) if f.endswith('.wav')]
    else:
        return []


def load_recording(path: str, file: str, n_fft: int, hop_length: int, n_mels: int, power_to_db: bool):
    """
    Return the Mel Spectogram for the recording in the wav file.
    The return dataframe has as columns the mel frequencies and rows the time in sec.
    """
    y, sr = librosa.load(os.path.join(path, file), sr=32000)
    # length = y.shape[0] / sr
    # write_log(f'File {file}: Sample rate is {sr/1000}kHz; Duration {length} (in secs)')

    mel_spectrogram = librosa.feature.melspectrogram(
        y=y,
        sr=sr,
        n_fft=n_fft,  # Size of my windows should be dynamic based on the sr
        hop_length=hop_length,
        n_mels=n_mels,  # How many freq bands do we need (TBTuned)
        power=1,  # We measure the energy of the signal (2 would be power)
    )

    if power_to_db:
        mel_spectrogram = librosa.power_to_db(mel_spectrogram)

    ret = pd.DataFrame(mel_spectrogram).transpose()
    ret['label'] = 0
    return ret


def project_label_recording(data: pd.DataFrame, start_indexes: list, end_indexes: list, hop_length: int, sr: int):
    if len(start_indexes) != len(end_indexes):
        #write_log('ERROR: The length for start and end index is different.')
        return pd.DataFrame()
    for i, start_index in enumerate(start_indexes):
        i_start = start_index * sr / hop_length
        i_end = end_indexes[i] * sr / hop_length
        data.loc[i_start:i_end, 'label'] = 1

    return data
