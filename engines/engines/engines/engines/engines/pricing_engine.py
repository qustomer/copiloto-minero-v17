def calculate_pricing(results):

    base_price = 10000

    risk_factor = (100 - results["ISP"]) / 100
    friction_factor = results["Friccion"] / 100
    complexity = results["IBH"] / 100

    price = base_price * (1 + risk_factor + friction_factor + complexity)

    return round(price, 2)
