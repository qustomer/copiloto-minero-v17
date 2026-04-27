import streamlit as st
import pandas as pd

from engines.ingestion_engine import run_ingestion_pipeline
from engines.scoring_engine import run_scoring_pipeline
from engines.warroom_engine import apply_solutions_and_recalculate
from engines.pricing_engine import calculate_pricing
from engines.proposal_pdf_generator import generate_dual_reports

st.set_page_config(layout="wide")
st.title("Copiloto Minero v17")

uploaded_files = st.file_uploader("Subir evidencia", accept_multiple_files=True)

eje = st.selectbox("Eje", ["Ambiental","Social","Gobernanza"])
calidad = st.selectbox("Calidad", ["Alta","Media","Baja"])
sentimiento = st.selectbox("Sentimiento", ["Positivo","Neutral","Negativo"])

if st.button("Procesar Ingesta") and uploaded_files:
    ingestion = run_ingestion_pipeline(uploaded_files,eje,calidad,sentimiento)
    st.session_state.docs = ingestion

if "docs" in st.session_state:
    df = st.session_state.docs["accepted"]
    st.write(df)

    if st.button("Ejecutar Scoring"):
        st.session_state.results = run_scoring_pipeline(df)

if "results" in st.session_state:
    res = st.session_state.results

    st.metric("IBH",res["IBH"])
    st.metric("Fricción",res["Friccion"])
    st.metric("ISP",res["ISP"])
    st.metric("ICG",res["ICG"])

    if st.button("Simular mejoras"):
        st.session_state.results = apply_solutions_and_recalculate(res)

    price = calculate_pricing(st.session_state.results)
    st.subheader(f"Honorarios estimados: USD {price}")

    if st.button("Generar PDF"):
        generate_dual_reports(st.session_state.results,price)
        st.success("PDF generado")
