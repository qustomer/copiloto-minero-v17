import hashlib
import pandas as pd

def file_hash(file):
    """Genera hash único del archivo"""
    return hashlib.md5(file.getvalue()).hexdigest()

def run_ingestion_pipeline(uploaded_files, eje, calidad, sentimiento):
    """
    Ingesta híbrida con filtro EDDF anti-eco
    """
    accepted_docs = []
    rejected_docs = []
    seen_hashes = set()

    for file in uploaded_files:
        h = file_hash(file)

        if h in seen_hashes:
            rejected_docs.append(file.name)
            continue

        seen_hashes.add(h)

        accepted_docs.append({
            "nombre": file.name,
            "eje": eje,
            "calidad": calidad,
            "sentimiento": sentimiento
        })

    return {
        "accepted": pd.DataFrame(accepted_docs),
        "rejected": rejected_docs
    }
