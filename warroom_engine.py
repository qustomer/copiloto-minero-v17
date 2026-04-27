def apply_solutions_and_recalculate(results):
    """
    Simula impacto de consultoría
    """

    improved = results.copy()

    improved["Friccion"] *= 0.7
    improved["ISP"] = min(95, results["ISP"] + 15)
    improved["IBH"] = min(100, results["IBH"] + 10)

    return improved
