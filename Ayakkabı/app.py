
from flask import Flask, render_template, request, redirect, url_for, flash
from data import get_categories, get_products, get_cart_items, add_to_cart, remove_from_cart

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Flash mesajları için gerekli

@app.route('/')
def home():
    categories = get_categories()
    return render_template('index.html', categories=categories)

@app.route('/products/<category_id>')
def products(category_id):
    products = get_products(category_id)
    return render_template('products.html', products=products, category_id=category_id)

@app.route('/cart')
def cart():
    cart_items, total_price = get_cart_items()
    return render_template('cart.html', cart_items=cart_items, total_price=total_price)

@app.route('/add-to-cart', methods=['POST'])
def add_product_to_cart():
    product_id = request.form.get('product_id')
    add_to_cart(product_id)
    flash("Ürün sepete eklendi!", "success")
    return redirect(url_for('cart'))

@app.route('/remove-from-cart', methods=['POST'])
def remove_product_from_cart():
    product_id = request.form.get('product_id')
    remove_from_cart(product_id)
    flash("Ürün sepetten kaldırıldı!", "warning")
    return redirect(url_for('cart'))

if __name__ == '__main__':
    app.run(debug=True)
