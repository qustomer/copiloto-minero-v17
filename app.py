# FORZAR ACTUALIZACION V17 NUEVO
import streamlit as st

st.set_page_config(layout="wide")
st.title("Copiloto Minero v17 - Nueva Version")

st.header("Subir evidencia")
archivo = st.file_uploader("Subi tu archivo", type=["pdf", "docx", "txt", "png", "jpg"])

if st.button("Procesar Ingesta"):
    if archivo:
        st.success(f"Archivo recibido: {archivo.name}")
        st.info("Ingesta procesada. Ahora podes seguir con el analisis.")
    else:
        st.warning("Primero subi un archivo arriba.")
