let totalPriceElement = document.querySelector('.total_price');
console.log(totalPriceElement.textContent);
const totalPrice = totalPriceElement.textContent;
const inputElement = document.getElementById('id_quantity');

// Add an event listener for the 'input' event
inputElement.addEventListener('input', (event) => {
    // Log the current value of the input field to the console
    console.log(event.target.value);
    totalPriceElement.textContent = totalPrice * event.target.value;
});