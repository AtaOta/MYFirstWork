// For Toggleing Navigation Bar
let Nave_Menu_Triger_In_Chat_Page = document.getElementById('Nave_Menu_Triger_In_Chat_Page');

Nave_Menu_Triger_In_Chat_Page.addEventListener('click', function(){
    navBar.classList.remove('HoverRight');
    navBar.classList.add('HoverLeft');
});

// Toggle Profile Section in chat-container
let Toggle_Profile_section =  document.querySelector('.Toggle_Down_Profile_Section');
let Chat_Page_Adjust = document.querySelector('.User_Chat_Display_Container');
Toggle_Profile_section.addEventListener('click', function(){
    Chat_Page_Adjust.classList.toggle('User_Chat_Display_Container_For_SmallScreen');

})


// Handelling message box and Chat section
let messageBoxDisplay = document.getElementById('message_box_Disppaly_Conatainer');
let Get_Receiver_Id = document.getElementById('Get_Receiver_Id');
let Scroll_Ydiraction_Container = document.getElementById('Scroll_Ydiraction_Container');

messageBoxDisplay.scrollTop = (Scroll_Ydiraction_Container.scrollHeight - messageBoxDisplay.clientHeight) + 50;

// This is For Sending and & Importing message
setInterval(function () { RequestChat(); }, 5000);

function RequestChat(){
    // console.log("Request 2 called");
//add request 2 code here
        
    url = `/chatting/chat_message_list/${Get_Receiver_Id.value}`;

    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4){
            Scroll_Ydiraction_Container.innerHTML = xhr.responseText;
            messageBoxDisplay.scrollTop = (Scroll_Ydiraction_Container.scrollHeight - messageBoxDisplay.clientHeight) + 50;
            
        }
    };
    xhr.open('GET', url);
    xhr.send();
}
