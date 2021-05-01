// For Hiding Search Box:
let Serch_box = document.querySelector('.Header_Search_Box');
Serch_box.style.opacity = '0';

// ==============[ For Capturing Image ]=================
var cameraStream = null;
// alert('This page is loaded');
let Video_Showing_Container = document.getElementById("Video_Showing_Container");
let Capture_Button_Holder = document.getElementById('Capture_Button_Holder');
let btnCapture = document.getElementById("btn-capture");
let btnTryAgain = document.getElementById( "btn-try-again" );
let Submition_Form = document.getElementById('Profile_Picture_Changing_Form');
let WhereToUseThe_Picture = document.getElementById('Where_To_Use_This_Picture');
let Set_Imge  = document.getElementById('UserPost_image_Preview');
let Beep1 = new Audio();
Beep1.src = "/media/Default/Sound/button-20.mp3";

// Streaming Start:
let mediaSupport = 'mediaDevices' in navigator;

if (mediaSupport && null == cameraStream) {

    navigator.mediaDevices.getUserMedia({ video: true })
        .then(function (mediaStream) {

            cameraStream = mediaStream;

            stream.srcObject = mediaStream;

            stream.play();
        })
        .catch(function (err) {

            console.log("Unable to access camera: " + err);
        });
}
else {

    alert('Your browser does not support media devices.');
}

// Capturing Image
btnCapture.addEventListener("click", captureSnapshot);

function captureSnapshot() {
    Beep1.play();
    if (null != cameraStream) {

        var ctx = capture.getContext('2d');
        var img = new Image();

        ctx.drawImage(stream, 0, 0, capture.width, capture.height);

        img.src = capture.toDataURL("image/png");
        img.width = 720;
        img.height = 480;

        Set_Imge.innerHTML = "";
        Set_Imge.appendChild( img );

    } else {
        alert('Your SnapShot does not work Properly.')
        return;
    }

    // This is for Showing Try Again Button
    btnCapture.classList.add('Hide_This');
    btnTryAgain.classList.remove('Hide_This');
    Video_Showing_Container.classList.add('Hide_This')
    Image_Showing_Container.classList.remove('Hide_This')
    WhereToUseThe_Picture.classList.remove('Hide_This');
}


// Try again Capture Your Image
btnTryAgain.addEventListener('click', captureTryAgain);
function captureTryAgain(){
    // This is for Showing Try Again Button
    btnCapture.classList.remove('Hide_This');
    btnTryAgain.classList.add('Hide_This');
    Video_Showing_Container.classList.remove('Hide_This')
    Image_Showing_Container.classList.add('Hide_This')
    WhereToUseThe_Picture.classList.add('Hide_This');
}

// Profile Picture Update Form Submission

Submition_Form.addEventListener('submit', function(e){
    e.preventDefault();

    let url = this.action;
    let image = document.getElementById("capture").toDataURL("image/png");
    let csrftoken = this.children[0].value;

    let ProfileImage_Data = new FormData();
    ProfileImage_Data.append('imageData', image);

    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4 && xhr.status === 200){
            WhereToUseThe_Picture.classList.add('Hide_This');
            Capture_Button_Holder.innerHTML = `<p>Your Profile Picture Is Upload Success-Fully</p>`;
        }
    };
    xhr.open('POST', url, true);
    xhr.setRequestHeader("X-CSRFToken", csrftoken);
    xhr.send(ProfileImage_Data);
})


// =====================[ Post Page Section ]=====================
let GoTo_PostCreate = document.getElementById('Create_Post_Target');
let GoTo_Previous_Page = document.getElementById('Previous_Page_Target');
let Post_Create_page = document.getElementById('Post_Create_Page');
let ImageCapture_Page  = document.getElementById('ImageCapture_Page_Inner_Container');
GoTo_PostCreate.addEventListener('click', function(){
    ImageCapture_Page.classList.add('ImageCapture_Page_Inner_Container_Hide_This');
    Post_Create_page.classList.remove('Hide_This');
})

GoTo_Previous_Page.addEventListener('click', function(){
    ImageCapture_Page.classList.remove('ImageCapture_Page_Inner_Container_Hide_This');
    Post_Create_page.classList.add('Hide_This');
})

// Profile Picture Update Form Submission
let CreatePost_Image_Form = document.getElementById('Capture_Normal_Post_Create_Form');
CreatePost_Image_Form.addEventListener('submit', function(e){
    e.preventDefault();
    

    let url = this.action;
    let Post_Subject = document.getElementById('id_subject').value;
    let image = document.getElementById("capture").toDataURL("image/png");
    let csrftoken = this.children[0].value;

    let PostImage_Data = new FormData();
    PostImage_Data.append('imageData', image);
    PostImage_Data.append('subject', Post_Subject);

    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4 && xhr.status === 200){
            ImageCapture_Page.classList.remove('ImageCapture_Page_Inner_Container_Hide_This');
            Post_Create_page.classList.add('Hide_This');
            WhereToUseThe_Picture.classList.add('Hide_This');
            Capture_Button_Holder.innerHTML = `<h4>Your Post Uploaded SuccessFully.</h4>`;
        }
    };
    xhr.open('POST', url, true);
    xhr.setRequestHeader("X-CSRFToken", csrftoken);
    xhr.send(PostImage_Data);
})

