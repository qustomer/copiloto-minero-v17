from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph

def generate_dual_reports(results, price):
    doc = SimpleDocTemplate("reporte.pdf", pagesize=letter)
    story = []

    text = f"""
    Resultados del Copiloto Minero

    IBH: {results['IBH']}
    Fricción: {results['Friccion']}
    ISP: {results['ISP']}
    ICG: {results['ICG']}

    Honorarios estimados: USD {price}
    """

    story.append(Paragraph(text))
    doc.build(story)
