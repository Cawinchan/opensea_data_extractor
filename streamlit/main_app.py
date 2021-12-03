import streamlit as st
import numpy as np
import io
import csv
import pandas as pd
import joblib

import matplotlib.pyplot as plt
import seaborn as sns

import librosa

y, sr = librosa.load('your_file.mp3')

st.title("NFT Audio Data Visualization")
st.header("Input and configuration")
st.subheader("Input files")
user_input = {}
user_input["input_csv"] = st.file_uploader(
    "Audio File (.mp3)"
)
if user_input["input_csv"]:
     y, sr = librosa.load(user_input["input_csv"])


