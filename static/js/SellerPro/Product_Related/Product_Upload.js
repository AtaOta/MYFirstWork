// :~~~~~~~~::~~~~~~~~::~~~~~~~~:[For Hiding Search Box:]:~~~~~~~~::~~~~~~~~::~~~~~~~~:
let Serch_box = document.querySelector('.Header_Search_Box');
Serch_box.style.opacity = '0';


// :~~~~~~~~::~~~~~~~~::~~~~~~~~:[Product Image Upload prevew]:~~~~~~~~::~~~~~~~~::~~~~~~~~:
const Product_Picture = document.getElementById("id_prod_picture");
const previewContainer_Product_Picture = document.getElementById("Product_Upload_image_Preview");
const previewImage_Product_pick = previewContainer_Product_Picture.querySelector(".Product_Upload_image_preview__image");
const previewDefaultText_Product_pick = previewContainer_Product_Picture.querySelector(".Product_Upload_image_preview_default_text");

Product_Picture.addEventListener("change", function(){
    const file = this.files[0];

    if (file){
        const reader = new FileReader();

        previewDefaultText_Product_pick.style.display = "none";
        previewImage_Product_pick.style.display = "block";
        reader.addEventListener("load", function(){
            previewImage_Product_pick.setAttribute("src", this.result);
        });
        reader.readAsDataURL(file);
    }
});




// :~~~~~~~~::~~~~~~~~::~~~~~~~~:[Form Validation In FontEnd]:~~~~~~~~::~~~~~~~~::~~~~~~~~:
let Products_Form = document.getElementById('products_form');
console.log(Products_Form);
// Product Name:-
let Product_Name_Input_Validator = document.getElementById('id_prod_name');
// Product Picture:-
let Product_Picture_Input_Validator = document.querySelector('.Product_Upload_image_preview__image');
let Image_Acceptor = document.getElementById('Image_Acceptor');
// Product Price:-
let Product_Price_Input_Validator = document.getElementById('id_prod_price');
// Product Quantity:-
let Product_Quantity_Input_Validator = document.getElementById('id_quantity');
// Product Description Text:-
let Product_DesText_Input_Validator = document.getElementById('id_prod_description');


// When the form will action to submit then we call this function
Products_Form.addEventListener('submit', Submitfunction);
function Submitfunction(event){
    event.preventDefault();

    // Validate Product Name:
    if (Product_Name_Input_Validator.value == ""){
        Product_Name_Input_Validator.placeholder = 'Please Enter Your Product Name';
        Product_Name_Input_Validator.classList.add('form_valid');
        return false;
    }

    // Validate Product Picture:
    Image_Acceptor.addEventListener('click', function(){
        document.getElementById('NoImage_Alert').innerText  = `Give A Product Picture.`;
        document.getElementById('NoImage_Alert').classList.remove('Validator_Text_Style');
        return false;

    })
    if (Product_Picture_Input_Validator.getAttribute('src') == ""){
        document.getElementById('NoImage_Alert').innerText = `Please Give Your Product Picture!`;
        document.getElementById('NoImage_Alert').classList.add('Validator_Text_Style');
        return false;
    }

    // Validate Product Price:
    if (Product_Price_Input_Validator.value == 0){
        Product_Price_Input_Validator.placeholder = '?';
        Product_Price_Input_Validator.value = '';
        Product_Price_Input_Validator.classList.add('form_valid');
        return false;
    }

    // Validate Product Quantity:
    if (Product_Quantity_Input_Validator.value == 0){
        Product_Quantity_Input_Validator.placeholder = '?';
        Product_Quantity_Input_Validator.value = '';
        Product_Quantity_Input_Validator.classList.add('form_valid');
        return false;
    }

    // Validate Description Text:
    if (Product_DesText_Input_Validator.value == ""){
        Product_DesText_Input_Validator.placeholder = 'Please Enter Product Description';
        Product_DesText_Input_Validator.classList.add('form_valid');
        return false;
    }

    // This Is Success Action:
    else{
        Products_Form.submit();
    }
}
