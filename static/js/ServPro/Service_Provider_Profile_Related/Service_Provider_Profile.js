console.log('this is service provider profile')
let Service_Provider_Product_Details = document.getElementById('Service_Provider_Product_Details')
let Product_Img = document.querySelectorAll('.Product_Img');
let Product_Image_shower_Container = document.getElementById('Product_Image_shower_Container');
let Return_form_Product_Details = document.querySelector('.Return_form_Product_Details');
let Top_Menu_Bar = document.getElementById('A_Top_menuBar');

if (Product_Img != null){

    Product_Img.forEach(clickProductPicture =>{
        clickProductPicture.addEventListener('click', function(){

            Service_Provider_Product_Details.classList.remove('Service_Provider_Product_Details_PopUp_Hide');
            Top_Menu_Bar.classList.remove('Toggle_top');

            Product_Image_shower_Container.innerHTML = `<img src="${this.src}" alt="">`;

            Return_form_Product_Details.addEventListener('click', function(e){
                Service_Provider_Product_Details.classList.add('Service_Provider_Product_Details_PopUp_Hide');
            })

        })
    })
}