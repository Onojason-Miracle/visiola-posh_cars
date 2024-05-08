document.querySelector("#quantity").addEventListener("input", function() {
    let quantity = parseInt(this.value);
    let pricePerDay = document.querySelector('#price'); 
    let rentAmount = document.querySelector('#amount')
    let totalPrice = quantity * pricePerDay;
    document.querySelector("#price").textContent = "Total Price: #" + totalPrice;

    rentAmount.value=totalPrice

  });