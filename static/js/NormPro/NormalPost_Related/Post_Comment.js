
let DisplayComments = document.querySelector('.posts_Comments_Display_section');
let User_Profile_Othere_Dynamic_Content_Container_Hide = document.getElementById('User_Profile_Othere_Dynamic_Content_Container_Hide');
let User_Profile_MessageBox_Popup_Container = document.getElementById('User_Profile_MessageBox_Popup_Container');
// console.log(User_Profile_MessageBox_Popup_Container)
// =============================[ This is For Comment Tiggering Section ]===========================
document.querySelectorAll('.User_Profile_Comment_Target').forEach(ClickCommentBtn =>{

    ClickCommentBtn.addEventListener('click', function(e){
        e.preventDefault;
        let CommentBtnId = this.id;
        // console.log(CommentBtnId)

        // ~~~~~~~#~~~~~~~#[ Add Comment Box ]#~~~~~~~#~~~~~~~
        User_Profile_Othere_Dynamic_Content_Container_Hide.classList.add('User_Profile_Othere_Dynamic_Content_Container_Hide');
        User_Profile_MessageBox_Popup_Container.classList.remove('User_Profile_MessageBox_Popup_Container_Hide');
        // console.log(User_Profile_MessageBox_Popup_Container);


        // ~~~~~~~#~~~~~~~#[ Add PopUp Image In Comment Section ]#~~~~~~~#~~~~~~~
        let PostImageLink = document.getElementById('NormalPost_Image_'+CommentBtnId);
        if (PostImageLink != null){
            // console.log(PostImageLink);
            PostImage = PostImageLink.src;
            let NormalPost_Image_Copy = document.querySelector('.NormalPost_Image_Copy_ImageAdd');
            NormalPost_Image_Copy.setAttribute("src", PostImage);
        }


        // ~~~~~~~#~~~~~~~#[ Close Comment Box ]#~~~~~~~#~~~~~~~
        document.querySelectorAll('.Remove_User_Profile_MessageBox_Popup_Container').forEach(RemoveCommentBox =>{

            RemoveCommentBox.addEventListener('click', function(event){
                event.preventDefault();
                User_Profile_MessageBox_Popup_Container.classList.add('User_Profile_MessageBox_Popup_Container_Hide');
                User_Profile_Othere_Dynamic_Content_Container_Hide.classList.remove('User_Profile_Othere_Dynamic_Content_Container_Hide');

            })
        });

    })
});


// =============================[ This is Display Comments ]===========================
document.querySelectorAll('.Load_NormalPost_Comments').forEach(ImportComments =>{

    ImportComments.addEventListener('click', function(e){
        e.preventDefault;
        let PostId = this.children[0].value;
        let Attached_PostId = document.getElementById('Normalr_post_Comments_Id');
        Attached_PostId.value = PostId;
        url = `/profile/List_comment/${PostId}`;
        DisplayComments.innerHTML = ``;

        var xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function() {
            if (xhr.readyState === 4){
                DisplayComments.innerHTML = xhr.responseText;
                
                // This For Comment Box Scrolling Purpose.
                DisplayComments.scrollTop = (DisplayComments.scrollHeight - DisplayComments.clientHeight) + 5;
            }
        };
        xhr.open('GET', url);
        xhr.send();

    })
})

// =============================[ For Creating Comments ]===========================
let PostSubmit_Foom = document.getElementById('NormalPost_Submition_Form');

PostSubmit_Foom.addEventListener('submit', function(e){
    e.preventDefault();
    let csrftoken = PostSubmit_Foom.children[0].value;
    let PostVal = PostSubmit_Foom.children[1].value;
    let PostIdVal = PostSubmit_Foom.children[2].value;
    url = `/profile/Create_comment`;

    let MsgData = new FormData();
    MsgData.append('NormalComment', PostVal)
    MsgData.append('NormalPostId', PostIdVal)

    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4 && xhr.status === 200){
            PostSubmit_Foom.children[1].value = "";
            DisplayComments.innerHTML = xhr.responseText;

            // This For Comment Box Scrolling Purpose.
            DisplayComments.scrollTop = (DisplayComments.scrollHeight - DisplayComments.clientHeight) + 5;
        }
    };
    xhr.open('POST', url, true);
    xhr.setRequestHeader("X-CSRFToken", csrftoken);
    xhr.send(MsgData);
})

