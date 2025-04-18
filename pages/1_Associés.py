
import streamlit as st
import pandas as pd

st.title("Gestion des Associés")

if "associates" not in st.session_state:
    st.session_state["associates"] = pd.DataFrame(columns=["Nom", "Rôle", "Engagement", "Entrée", "Sortie"])

with st.form("add_associate"):
    nom = st.text_input("Nom")
    role = st.selectbox("Rôle", ["Médecin", "Infirmier", "Kiné", "Autre"])
    engagement = st.selectbox("Type d'engagement", ["Temps plein", "Temps partiel"])
    entree = st.date_input("Date d'entrée")
    sortie = st.date_input("Date de sortie", disabled=True)
    submit = st.form_submit_button("Ajouter")

    if submit:
        new_row = {"Nom": nom, "Rôle": role, "Engagement": engagement, "Entrée": entree, "Sortie": sortie}
        st.session_state["associates"] = st.session_state["associates"].append(new_row, ignore_index=True)

st.subheader("Liste des Associés")
st.dataframe(st.session_state["associates"])
