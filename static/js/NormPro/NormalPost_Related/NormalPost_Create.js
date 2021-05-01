// For Hiding Search Box:
let Serch_box = document.querySelector('.Header_Search_Box');
Serch_box.style.opacity = '0';


// This is for handeling Image in post:
const inpFile = document.getElementById("id_post_pick");
const previewContainer = document.getElementById("UserPost_image_Preview");
const previewImage = previewContainer.querySelector(".UserPost_image_preview__image");
const previewDefaultText = previewContainer.querySelector(".UserPost_image_preview_default_text");

inpFile.addEventListener("change", function(){
    const file = this.files[0];

    if (file){
        const reader = new FileReader();

        previewDefaultText.style.display = "none";
        previewImage.style.display = "block";
        reader.addEventListener("load", function(){
            previewImage.setAttribute("src", this.result);
        });
        reader.readAsDataURL(file);
    }
});