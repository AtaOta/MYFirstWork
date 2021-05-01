
    // =============================[ This is For Showing More Details Of an User ]===========================
let User_Profile_More_Details_Link = document.getElementById('User_Profile_More_Details_Link');
//    console.log(User_Profile_More_Details_Link)
User_Profile_More_Details_Link.addEventListener('click', function(e){
    let User_Profile_Deatis_Holder_Container_Hide = document.getElementById('User_Profile_Deatis_Holder_Container_Hide');
    User_Profile_Deatis_Holder_Container_Hide.classList.toggle('User_Profile_Deatis_Holder_Container_Hide');
    if (User_Profile_More_Details_Link.innerHTML === "More") {
        User_Profile_More_Details_Link.innerHTML = "Less";
        User_Profile_More_Details_Link.style = 'color: red';
    } else {
        User_Profile_More_Details_Link.innerHTML = "More";
        User_Profile_More_Details_Link.style = 'color: #159AC4;';
    }
});


