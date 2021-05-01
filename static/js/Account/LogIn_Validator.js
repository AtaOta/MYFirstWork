
// Validate Other Input:
//Import Form:
let LogIn_Form = document.getElementById('Login_Form');

// When The Form is Submitted Trigger Tis Function
LogIn_Form.addEventListener('submit', Submitfunction);
function Submitfunction(e) {
    e.preventDefault();  

    // Validate User Name:
    username.addEventListener('click', function(){
        Check_User_name.innerHTML = ``;
    })
    if(username.value == ""){
        Check_User_name.innerHTML = `Please Enter Your User Name`;
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
    re = /^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$/;
    if(!re.test(Input_password.value)){
        check_Password.innerHTML = `At least one upper case English letter,
        At least one lower case English letter,
        At least one digit,
        At least one special character, Minimum 8 to 40 in Length`;
        return false;
    }
    
    // This Is Success Action:
    else{
//        location.reload(true);
//        window.location.href = this.action;
        LogIn_Form.submit();
    }
    
}