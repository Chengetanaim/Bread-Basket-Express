const errorElements = document.querySelectorAll('.errorlist');

// Apply styles to each element
errorElements.forEach(element => {
    element.style.color = 'red';
    element.style.backgroundColor = '#fdd';
    element.style.border = '1px solid red';
    element.style.padding = '10px';
    element.style.margin = '10px 0';
    element.style.fontWeight = 'bold';
});