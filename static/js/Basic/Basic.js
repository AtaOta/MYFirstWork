// Getting The Page loader
let loader = document.querySelector('.Loader_Holder');
let Toggle_Top_ScrollBar_Triger = document.getElementById('Toggle_Down_Top_ScrollBar_Triger');

// Window Load Function Start From Here:
window.onload = function(){

    // Hiding Page Loader
    loader.classList.add('Display_None');


    // // Scroll Check UP 
    var section = document.getElementsByTagName('section')[0];
    let top_menuBar = document.getElementById('A_Top_menuBar');
    if (top_menuBar.classList != "Toggle_top"){
        section.onscroll = function() {
            let Y = section.scrollTop;
            if(Y> 50){
                top_menuBar.classList.add('Toggle_top');
                Toggle_Top_ScrollBar_Triger.classList.remove('Hide_Content');
                
                // Top Scroll Tiger Button Workin Program:
                Toggle_Top_ScrollBar_Triger.addEventListener('click', function(){
                    top_menuBar.classList.remove('Toggle_top');
                    Toggle_Top_ScrollBar_Triger.classList.add('Hide_Content');

                });
            }else{
                top_menuBar.classList.remove('Toggle_top');
                Toggle_Top_ScrollBar_Triger.classList.add('Hide_Content');
            }
        }
    }
    else{
        top_menuBar.classList.remove('Toggle_top');
    }
    
    // Hiding Top Content
    let Content_Top_Of_Page = document.getElementById('Content_Top_Of_Page');

    if (Content_Top_Of_Page.innerHTML.length <= 20){
        Content_Top_Of_Page.classList.add('Hide_Content');
    }
}


// // Select All Another Page Routher Anchor Tag
    // document.querySelectorAll('.A_Triger').forEach(Another_Page_Router => {

    //     // Tergate The Anchor Button
    //     Another_Page_Router.addEventListener('click', function(e){
    //         e.preventDefault();
    //         let url = this.href;
    //         var xhttp = new XMLHttpRequest();
    //         xhttp.onreadystatechange = function() {
    //             if (this.readyState == 4 && this.status == 200) {
    //               document.getElementById("A_PageVue").innerHTML = this.responseText;
    //             }
    //           };
    //           xhttp.open("GET", url , true);
    //           xhttp.send();
    //     })
    // })

