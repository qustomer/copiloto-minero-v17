import random

def run_scoring_pipeline(df_docs):
    """
    Motor pericial simplificado
    """

    n_docs = len(df_docs)

    IBH = min(100, n_docs * 0.8)
    friccion = max(5, 60 - n_docs * 0.3)
    ISP = max(10, min(95, IBH - friccion + random.uniform(-5,5)))
    ICG = min(100, n_docs * 0.9)

    return {
        "IBH": round(IBH,1),
        "Friccion": round(friccion,1),
        "ISP": round(ISP,1),
        "ICG": round(ICG,1),
        "n_docs": n_docs
    }
