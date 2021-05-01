let Dleete_Message_comfirmation_Container = document.getElementById('Profile_Page_User_Action_Confirmation_Container');
let DeleteConfirmation_Message_Box = document.querySelector('.Profile_Page_Confirmation_Card');
let DeletePost_NoteSure_Button = document.querySelector('.ProfilePage_Confirmation_NoteSure_Button');
let DeletePost_Sure_Button = document.querySelector('.ProfilePage_Confirmation_Sure_Button');
let csrf_token_Input = document.getElementById('csrf_token_Input');
let NormalPost_Delete_Id = document.getElementById('NormalPost_Delete_Id');


document.querySelectorAll('.Delete_The_NormalPost').forEach(DeleteNormalPost =>{

    DeleteNormalPost.addEventListener('submit', function(e){
        e.preventDefault();
        let DeleteUrl = this.action;
        let Csrf_value = this.children[0].value;
        let PostId = this.children[1].value;

        Dleete_Message_comfirmation_Container.classList.remove('Profile_Page_User_Action_Confirmation_Container_Hide');

        DeletePost_NoteSure_Button.addEventListener('click', function(){
            Dleete_Message_comfirmation_Container.classList.add('Profile_Page_User_Action_Confirmation_Container_Hide');
        })

        // Adding Action Url Confirmation message box
        DeletePost_Sure_Button.value = `${DeleteUrl}`;
        csrf_token_Input.value = `${Csrf_value}`;
        NormalPost_Delete_Id.value = `${PostId}`;
        

    })
})

DeletePost_Sure_Button.addEventListener('click', function(){
    let url = DeletePost_Sure_Button.value;
    let csrftoken = csrf_token_Input.value;
    let fadeOut_PostId = NormalPost_Delete_Id.value;
    let fadeOut_Post = document.getElementById('Target_FadeOut_This_Dive_Delete_The_NormalPost'+fadeOut_PostId);

    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4 && xhr.status === 200){

            if (xhr.responseText === 'true'){
                Dleete_Message_comfirmation_Container.classList.add('Profile_Page_User_Action_Confirmation_Container_Hide');
                fadeOut_Post.style.display = 'none';

            }
        }
    };
    xhr.open('POST', url, true);
    xhr.setRequestHeader("X-CSRFToken", csrftoken);
    xhr.send();
})

