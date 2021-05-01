document.querySelectorAll('.Action_Follow_UnFollow').forEach(Action_To_Follow =>{

    Action_To_Follow.addEventListener('click', function(event){
        event.preventDefault();

        let Follow_Url = this.href;
        let Follow_UnFollow_Button = this;

        var xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function(){
            if (xhr.readyState === 4){

                if (xhr.responseText == 'True'){
                    Follow_UnFollow_Button.innerHTML = `
                    <button class="All_User_List_Container_Inner_Content_UnFollow_Button">
                        <img src="/static/Icon/NormPro/IconsForFollow_UnFollow/unfollow.svg" alt="">
                        Un Follow
                    </button>`;
                }
                else if(xhr.responseText == 'False'){
                    Follow_UnFollow_Button.innerHTML = `
                    <button class="All_User_List_Container_Inner_Content_Follow_Button">
                        <img src="/static/Icon/NormPro/IconsForFollow_UnFollow/follower.svg" alt="">
                        Follow
                    </button>`;
                }
                else{
                    console.log('Something Going Wrong');
                }
            }
        };
        xhr.open('GET', Follow_Url);
        xhr.send();
    })
})