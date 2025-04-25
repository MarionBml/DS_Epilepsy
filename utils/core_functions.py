import os
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

def write_log(log: str):
    formatted_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f'{formatted_datetime} - {log} ...')
    with open(os.path.join(ROOT, 'logs', 'output.log'), 'a') as f:
        f.write(f'{formatted_datetime} - {log} ...')
        f.write('\n')

def plot(signal, sr, flags, file):
    plt.figure(figsize=(20, 8))
    length = signal.shape[0] / sr
    time = np.linspace(0., length, signal.shape[0])
    plt.scatter(
        x=time,
        y=signal,
        c=flags,
        s=1,
    )
    plt.xlabel("Time [s]")
    plt.ylabel("Amplitude")
    plt.title(f'Raw Signal for {file}')
    plt.savefig(os.path.join(OUTPUT_PATH,f'Fig {file}.png'), format='png', dpi=100)  # dpi=300 for high resolution
    return None