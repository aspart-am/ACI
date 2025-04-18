
import streamlit as st
import pandas as pd

st.title("Synthèse des Rémunérations")

# Simulation basique à ajuster avec indicateurs et missions
if "missions" in st.session_state:
    st.subheader("Calcul basé sur les missions")
    df = st.session_state["missions"]
    summary = df.groupby("Associé")["Durée (h)"].sum().reset_index()
    summary["Montant estimé (€)"] = summary["Durée (h)"] * 30  # Exemple : 30€/h
    st.table(summary)
else:
    st.info("Aucune mission enregistrée.")
