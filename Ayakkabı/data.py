
CATEGORIES = {
    "kosu": "Koşu Ayakkabıları",
    "antrenman": "Antrenman Ayakkabıları",
    "lifestyle": "Lifestyle Ayakkabılar"
}

PRODUCTS = {
    "kosu": [{"id": f"kosu_{i}", "name": f"Koşu Ayakkabı {i}", "price": 499 + i * 10, "image": f"/static/images/kosu_{i}.jpg"} for i in range(1, 31)],
    "antrenman": [{"id": f"antrenman_{i}", "name": f"Antrenman Ayakkabı {i}", "price": 599 + i * 10, "image": f"/static/images/antrenman_{i}.jpg"} for i in range(1, 31)],
    "lifestyle": [{"id": f"lifestyle_{i}", "name": f"Lifestyle Ayakkabı {i}", "price": 699 + i * 10, "image": f"/static/images/lifestyle_{i}.jpg"} for i in range(1, 31)]
}

CART = []

def get_categories():
    return CATEGORIES

def get_products(category_id):
    return PRODUCTS.get(category_id, [])

def get_cart_items():
    total_price = sum(item['price'] for item in CART)
    return CART, total_price

def add_to_cart(product_id):
    for category, items in PRODUCTS.items():
        for product in items:
            if product["id"] == product_id:
                CART.append(product)
                return

def remove_from_cart(product_id):
    global CART
    CART = [item for item in CART if item["id"] != product_id]
