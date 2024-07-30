# Set web page format
import streamlit as st
st.set_page_config(layout="wide")
# Diasble virtual VRAM on windows system
import torch
torch.cuda.set_per_process_memory_fraction(0.999, 0)


st.markdown("""
# DiffSynth Studio

[Source Code](https://github.com/TinsleyME/DiffSynth-Studio-openxlab)

Welcome to DiffSynth Studio.
""")
import os
os.system(f"python ModelDownload.py")
