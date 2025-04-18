
import streamlit as st
import pandas as pd

st.title("Indicateurs ACI")

uploaded_file = st.file_uploader("Importer un fichier Excel d'indicateurs", type=["xlsx"])

if uploaded_file:
    df = pd.read_excel(uploaded_file)
    st.session_state["indicateurs"] = df
    st.success("Fichier importé avec succès.")

if "indicateurs" in st.session_state:
    st.subheader("Indicateurs chargés")
    st.dataframe(st.session_state["indicateurs"])
