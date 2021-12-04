import streamlit as st
import numpy as np
import io

import matplotlib.pyplot as plt

import librosa
import librosa.display

from pydub import AudioSegment

def read_fileuploader(file_uploader_bytes):
    bytesio = io.BytesIO(file_uploader_bytes)
    sound = AudioSegment.from_file(bytesio, format=user_input["input_csv"].name.split(".")[-1])
    channel_sounds = sound.split_to_mono()
    samples = [s.get_array_of_samples() for s in channel_sounds]

    fp_arr = np.array(samples).T.astype(np.float32)
    fp_arr /= np.iinfo(samples[0].typecode).max

    return fp_arr[:, 0], sound.frame_rate


st.title("NFT Audio Data Visualization")
st.header("Input and configuration")
st.subheader("Input files")
user_input = {}
user_input["input_csv"] = st.file_uploader(
    "Audio File (.mp3)"
)    

if user_input["input_csv"]:

    st.write("Sound Audio Plots:")
    y, sr = read_fileuploader(user_input["input_csv"].read())
    fig, ax = plt.subplots()
    img = librosa.display.waveplot(y, sr=sr, x_axis='time', ax=ax)
    ax.set(title='Waveplot')
    st.pyplot(plt.gcf())

    S = librosa.feature.melspectrogram(y, sr=sr)
    S_dB = librosa.power_to_db(S, ref=np.max)
    img = librosa.display.specshow(S_dB, x_axis='time',
                            y_axis='mel', sr=sr,
                            fmax=8000, ax=ax)
    fig.colorbar(img, ax=ax, format='%+2.0f dB')
    ax.set(title='Mel-frequency spectrogram')
    st.pyplot(plt.gcf())

    chroma = librosa.feature.chroma_stft(y, sr=sr)
    img = librosa.display.specshow(chroma, y_axis='chroma', x_axis='time', ax=ax)
    fig.colorbar(img, ax=ax)
    ax.set(title='Chromagram')
    st.pyplot(plt.gcf())

    hop_length = 512
    oenv = librosa.onset.onset_strength(y=y, sr=sr, hop_length=hop_length)
    tempogram = librosa.feature.tempogram(onset_envelope=oenv, sr=sr,
                                        hop_length=hop_length)
    # Compute global onset autocorrelation
    ac_global = librosa.autocorrelate(oenv, max_size=tempogram.shape[0])
    ac_global = librosa.util.normalize(ac_global)

    fig, ax = plt.subplots(nrows=4, figsize=(10, 10))
    # Estimate the global tempo for display purposes
    tempo = librosa.beat.tempo(onset_envelope=oenv, sr=sr,
                            hop_length=hop_length)[0]
    times = librosa.times_like(oenv, sr=sr, hop_length=hop_length)
    ax[0].plot(times, oenv, label='Onset strength')
    ax[0].label_outer()
    ax[0].legend(frameon=True)
    librosa.display.specshow(tempogram, sr=sr, hop_length=hop_length,
                            x_axis='time', y_axis='tempo', cmap='magma',
                            ax=ax[1])
    ax[1].axhline(tempo, color='w', linestyle='--', alpha=1,
                label='Estimated tempo={:g}'.format(tempo))
    ax[1].legend(loc='upper right')
    ax[1].set(title='Tempogram')
    x = np.linspace(0, tempogram.shape[0] * float(hop_length) / sr,
                    num=tempogram.shape[0])
    ax[2].plot(x, np.mean(tempogram, axis=1), label='Mean local autocorrelation')
    ax[2].plot(x, ac_global, '--', alpha=0.75, label='Global autocorrelation')
    ax[2].set(xlabel='Lag (seconds)')
    ax[2].legend(frameon=True)
    freqs = librosa.tempo_frequencies(tempogram.shape[0], hop_length=hop_length, sr=sr)
    ax[3].semilogx(freqs[1:], np.mean(tempogram[1:], axis=1),
                label='Mean local autocorrelation', basex=2)
    ax[3].semilogx(freqs[1:], ac_global[1:], '--', alpha=0.75,
                label='Global autocorrelation', basex=2)
    ax[3].axvline(tempo, color='black', linestyle='--', alpha=.8,
                label='Estimated tempo={:g}'.format(tempo))
    ax[3].legend(frameon=True)
    ax[3].set(xlabel='BPM')
    ax[3].grid(True)
    st.pyplot(plt.gcf())

