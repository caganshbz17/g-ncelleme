
document.addEventListener('DOMContentLoaded', () => {
    const categories = {
        kosu: 'Koşu Ayakkabıları',
        antrenman: 'Antrenman Ayakkabıları',
        lifestyle: 'Lifestyle Ayakkabılar'
    };

    const productList = document.querySelector('.product-list');
    const cart = []; // Sepet için dizi

    function updateCart() {
        const cartSection = document.getElementById('cart-items');
        cartSection.innerHTML = '';
        cart.forEach((item, index) => {
            const itemDiv = document.createElement('div');
            itemDiv.className = 'cart-item';
            itemDiv.innerHTML = `
                <p>${item.name} - ${item.price}</p>
                <button onclick="removeFromCart(${index})">Kaldır</button>
            `;
            cartSection.appendChild(itemDiv);
        });
    }

    window.removeFromCart = (index) => {
        cart.splice(index, 1);
        updateCart();
    };

    function generateProducts(category) {
        productList.innerHTML = ''; // Eski ürünleri temizle
        for (let i = 1; i <= 30; i++) {
            const productDiv = document.createElement('div');
            productDiv.className = 'product';
            const productName = `${categories[category]} - Model ${i}`;
            const productPrice = `₺${499 + i * 10}`;
            productDiv.innerHTML = `
                <img src="https://via.placeholder.com/300x200" alt="${categories[category]} Ayakkabı ${i}">
                <h3>${productName}</h3>
                <p>${productPrice}</p>
                <button onclick="addToCart('${productName}', '${productPrice}')">Satın Al</button>
            `;
            productList.appendChild(productDiv);
        }
    }

    window.addToCart = (name, price) => {
        cart.push({ name, price });
        updateCart();
        alert('Ürün sepete eklendi!');
    };

    document.getElementById('kosu').addEventListener('click', () => generateProducts('kosu'));
    document.getElementById('antrenman').addEventListener('click', () => generateProducts('antrenman'));
    document.getElementById('lifestyle').addEventListener('click', () => generateProducts('lifestyle'));

    document.getElementById('discover-button').addEventListener('click', () => {
        alert('Yeni sezon ürünlerimize göz atın!');
    });

    console.log('Sayfa başarıyla yüklendi.');
});
