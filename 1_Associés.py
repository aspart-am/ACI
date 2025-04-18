
import streamlit as st
import pandas as pd

st.title("Gestion des Associés")

uploaded_file = st.file_uploader("Importer un fichier Excel avec les associés")
if uploaded_file:
    df = pd.read_excel(uploaded_file)
    st.dataframe(df)
