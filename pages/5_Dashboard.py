
import streamlit as st
import plotly.express as px
import pandas as pd

st.title("Dashboard")

if "missions" in st.session_state:
    df = st.session_state["missions"]
    if not df.empty:
        fig = px.bar(df, x="Associé", y="Durée (h)", color="Mission", title="Temps passé par mission")
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("Pas de missions à afficher.")
else:
    st.info("Chargez d'abord des missions.")
