document.querySelector("#quantity").addEventListener("input", function() {
    let quantity = parseInt(this.value);
    let pricePerDay = 50000; 
    let totalPrice = quantity * pricePerDay;
    document.querySelector("#price").textContent = "Total Price: #" + totalPrice.toFixed(2);
  });