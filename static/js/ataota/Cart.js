let CartCounter = document.getElementById('Cart_Product_Count');

// This Part Is For Add To Cart
let Add_To_Cart = document.querySelectorAll('.Add_To_Cart');


if (Add_To_Cart != null){

    Add_To_Cart.forEach(clickToCart => {
        clickToCart.addEventListener('click', function(e){
            let productId = this.id;
            let action = this.value;

            // console.log('USER:', user)
            if (user === 'AnonymousUser'){
                console.log('User is not authenticated');
                localStorage.clear();
            }else{
                updateUserOrder(productId, action)
            }
        })
    })
}

function updateUserOrder(productId, action){
    // console.log('User is authenticated, sending data...');
    var url = '/seller/update_cart_item/'

    fetch(url, {
        method: 'POST',
        headers:{
            'Content-Type': 'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'productId': productId, 'action': action})
    })
    .then((response) =>{
        return response.json();
    })
    .then((data) => {
        let CartData = eval(data);

        // Add data to local storage:
        localStorage.setItem('Product_Quantity', CartData[0].ItemQuantity);
            // console.log(CartCounter);
        CartCounter.innerHTML = localStorage.getItem('Product_Quantity');
        CartCounter.style.opacity = 1;
    })
}



// This Part Is For Remove Form Cart
let Remove_Cart_Product = document.querySelectorAll('.Remove_Cart_Product');

if (Remove_Cart_Product != null){

    Remove_Cart_Product.forEach(removeToCart => {
        removeToCart.addEventListener('click', function(e){
            let productId = this.id;
            let action = this.value;

            if (user === 'AnonymousUser'){
                console.log('User is not authenticated');
                localStorage.clear();
            }else{
                removeProductFormCart(productId, action)
            }

        })
    })
}

function removeProductFormCart(productId, action){
    // console.log('User is authenticated, sending data...');
    var url = '/seller/remove_cart_item/'

   fetch(url, {
       method: 'POST',
       headers:{
           'Content-Type': 'application/json',
           'X-CSRFToken':csrftoken,
       },
       body:JSON.stringify({'productId': productId, 'action': action})
   })
   .then((response) =>{
       return response.json();
   })
   .then((data) => {
       let CartData = eval(data);

       if (CartData[0].SetItem != 'Removed'){
            let cartListContainer = document.getElementById(productId);
            let Particular_container = cartListContainer.parentNode.parentNode.children[3];
            Particular_container.children[1].value = CartData[0].SetItem;
            document.getElementById('Total_Products_FinalCount').innerText = CartData[0].ItemQuantity;

            // Add data to local storage:
            localStorage.setItem('Product_Quantity', CartData[0].ItemQuantity);
            CartCounter.innerHTML = localStorage.getItem('Product_Quantity');
       }

       if (CartData[0].SetItem === 'Removed'){
           let cartListContainer = document.getElementById(productId);
           let Particular_container = cartListContainer.parentNode.parentNode.parentNode;
           Particular_container.classList.add('Hide_Content');
           document.getElementById('Total_Products_FinalCount').innerText = CartData[0].ItemQuantity;

           // Add data to local storage:
           localStorage.setItem('Product_Quantity', CartData[0].ItemQuantity);
           CartCounter.innerHTML = localStorage.getItem('Product_Quantity');
           
       }
   })
}

// For globally access The Cart:
CartCounter.innerHTML = localStorage.getItem('Product_Quantity');
if (CartCounter.innerText == 0){
    CartCounter.style.opacity = 0;
}else{
    CartCounter.style.opacity = 1;
}
