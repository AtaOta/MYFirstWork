let Show_NavBar_Triger = document.getElementById('Show_NavBar_Triger');
let navBar = document.getElementsByTagName('nav')[0];
let nav_Hider = document.getElementById('A_Nave_Hider');
// console.log(Show_NavBar_Triger);

var start = null;
window.addEventListener("touchstart",function(event){
if(event.touches.length === 1){
        //just one finger touched
        start = event.touches.item(0).clientX;
        // console.log(start);
    }else{
        //a second finger hit the screen, abort the touch
        start = null;
    }
});

window.addEventListener("touchend",function(event){
    var offset = 100;//at least 100px are a swipe
    if(start){
        //the only finger that hit the screen left it
        var end = event.changedTouches.item(0).clientX;
    //   console.log(navBar);
        

        if(end > (start + offset) && (end-start) > 150){
        //a left -> right swipe
            navBar.classList.add('HoverRight');
            navBar.classList.remove('HoverLeft');

            // console.log(end-start);
        }
        if(end < (start - offset) && (start-end) > 300){
        //a right -> left swipe
            navBar.classList.remove('HoverRight');
            navBar.classList.add('HoverLeft');
        }
    }
});

Show_NavBar_Triger.addEventListener('click', function(){
    navBar.classList.remove('HoverRight');
    navBar.classList.add('HoverLeft');
});

nav_Hider.addEventListener('click', function(){
    navBar.classList.add('HoverRight');
    navBar.classList.remove('HoverLeft');
})