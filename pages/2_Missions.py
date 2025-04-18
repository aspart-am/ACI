
import streamlit as st
import pandas as pd

st.title("Suivi des Missions")

if "missions" not in st.session_state:
    st.session_state["missions"] = pd.DataFrame(columns=["Associé", "Mission", "Durée (h)"])

with st.form("add_mission"):
    associe = st.text_input("Nom de l'associé")
    mission = st.text_input("Nom de la mission")
    duree = st.number_input("Durée (heures)", min_value=0.0)
    submit = st.form_submit_button("Ajouter la mission")

    if submit:
        new_row = {"Associé": associe, "Mission": mission, "Durée (h)": duree}
        st.session_state["missions"] = st.session_state["missions"].append(new_row, ignore_index=True)

st.subheader("Missions enregistrées")
st.dataframe(st.session_state["missions"])
