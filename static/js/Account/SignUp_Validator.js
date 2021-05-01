// ==============[ This section is for Password In SignUp Form ]=================
var Password_Visibility = document.getElementById("Password_icon_In_S");
let Input_password = document.getElementById("id_password");
let password = true;

// This is for SignUp Form Password Hide and show
Password_Visibility.addEventListener('click', function(){
    if (password){
        Input_password.setAttribute('type', 'text');
        Password_Visibility.innerHTML = `
        <img src="/static/Icon/Account/visibility.svg" alt="VisibleIcon">
        `;
    }else{
        Input_password.setAttribute('type', 'password');
        Password_Visibility.innerHTML = `
        <img src="/static/Icon/Account/invisible.svg" alt="InvisibleIcon">
        `;

    }
    password =! password;
})

// This section is for ConfirmPassword Hide and show
var Confirm_Password_Visibility = document.getElementById("ConfirmPassword_icon_In_S");
let Confirm_Input_password = document.getElementById("id_re_password");
Confirm_Password_Visibility.addEventListener('click', function(){
    if (password){
        Confirm_Input_password.setAttribute('type', 'text');
        Confirm_Password_Visibility.innerHTML = `
        <img src="/static/Icon/Account/visibility.svg" alt="VisibleIcon">
        `;
    }else{
        Confirm_Input_password.setAttribute('type', 'password');
        Confirm_Password_Visibility.innerHTML = `
        <img src="/static/Icon/Account/invisible.svg" alt="InvisibleIcon">
        `;

    }
    password =! password;
})

// Validate Other Input:
//Import Form:
let SignUp_Form = document.getElementById('SignUp_Form');

//Basic Input Tags:
let Full_Name = document.getElementById('id_full_name');
let username = document.getElementById('id_username');
let email = document.getElementById('id_email');



// Span Content (Check Up text Holder):
let Check_first_name = document.querySelector('.Check_first_name');
let Check_User_name = document.querySelector('.Check_User_name');
let check_Email = document.querySelector('.check_Email');
let check_Password = document.querySelector('.check_Password');
let check_Re_Password = document.querySelector('.check_Re_Password');


if (SignUp_Form != null) {
    // When The Form is Submitted Trigger Tis Function
    SignUp_Form.addEventListener('submit', Submitfunction);
    function Submitfunction(e) {
        e.preventDefault();    
        
        // Validate Full Name:
        Full_Name.addEventListener('click', function(){
            Check_first_name.innerHTML = ``;
        })
        if (Full_Name.value == ""){
            Check_first_name.innerHTML = `Please Enter Your Full Name`;
            return false;
        }    
        if ((Full_Name.value.length) <=6  || (Full_Name.value.length) > 20 ){
            Check_first_name.innerHTML = `Your Name Should Contains 7 to 20 Chracter`;
            return false;
        }

        // Validate User Name:
        username.addEventListener('click', function(){
            Check_User_name.innerHTML = ``;
        })
        if(username.value == ""){
            Check_User_name.innerHTML = `Please Enter Your User Name`;
            return false;
        }
        if(username.value == Full_Name.value){
            Check_User_name.innerHTML = `User Name Should be different from Full Name`;
            return false;
        }

        // Validate Email:
        email.addEventListener('click', function(){
            check_Email.innerHTML = ``;
        })
        if(email.value == ""){
            check_Email.innerHTML = `Please Enter email`;
            return false;
        }
        re = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
        if(!re.test(email.value)){
            check_Email.innerHTML = `Please Enter A Valid email`;
            return false;
        }

        // Validate Password:
        Input_password.addEventListener('click', function(){
            check_Password.innerHTML = ``;
        })
        if(Input_password.value == ""){
            check_Password.innerHTML = `Please Enter Your Password`;
            return false;
        }
        if(Input_password.value.length > 40){
            check_Password.innerHTML = `Password contains Maximum 40 Character`;
            return false;
        }
        if(Input_password.value == username.value){
            check_Password.innerHTML = `Your Password Should Be Different From Full-Name, email & User-Name`;
            return false;
        }
        re = /^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$/;
        if(!re.test(Input_password.value)){
            check_Password.innerHTML = `At least one upper case English letter,
            At least one lower case English letter,
            At least one digit,
            At least one special character, Minimum 8 to 40 in Length`;
            return false;
        }

        // Validate Re Password:
        Confirm_Input_password.addEventListener('click', function(){
            check_Re_Password.innerHTML = ``;
            Confirm_Input_password.value = "";
        })
        if(Confirm_Input_password.value == ""){
            check_Re_Password.innerHTML = `Please Enter Your Password Again`;
            return false;
        }
        if(Input_password.value != Confirm_Input_password.value){
            check_Re_Password.innerHTML = `Your 2nd Password Don't Match`;
            return false;
        }

        // This Is Success Action:
        else{
//            window.location = this.action;
            SignUp_Form.submit();
        }
    }
}