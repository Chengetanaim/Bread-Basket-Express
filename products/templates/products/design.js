function orderProduct(productName, productPrice) {
    document.getElementById('product').value = productName;
    document.getElementById('price').value = `$${productPrice.toFixed(2)}`;
    document.getElementById('order-form').scrollIntoView();
}

document.getElementById('form').addEventListener('submit', function(event) {
    event.preventDefault();
    alert('Thank you for your order!');
    this.reset();
});
