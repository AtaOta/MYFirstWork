let Profile_Toggler = document.querySelector('.Toggle_Down_Profile_Section');
let Fixd_Profile_Section = document.querySelector('.User_Profile_Fixed_Content_Container');
let Fixed_Profile_Toggler_Image = document.getElementById('Fixed_Profile_Toggler_Image');

Profile_Toggler.addEventListener('click', function(){
    // alert('clicked Profile Toggler');
    Fixd_Profile_Section.classList.toggle('Hide_Profile_For_ChatList');
    Fixed_Profile_Toggler_Image.classList.toggle('Fixed_Profile_Toggler_Image');

})


