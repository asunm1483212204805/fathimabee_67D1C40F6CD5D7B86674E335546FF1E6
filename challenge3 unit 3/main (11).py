def linear_search_product(products, target_product):
    indices = []
    for i, product in enumerate(products):
        if product == target_product:
            indices.append(i)
    return indices
products = ["ORANGE", "BANANA", "MANGO", "KIWI", "APPLE"]
target_product = "APPLE"
result = linear_search_product(products, target_product)
print("Indices of", target_product, ":", result)