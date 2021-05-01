document.querySelectorAll('.Normal_Post_Like_Dislike_Action').forEach(clickLike => {
    clickLike.addEventListener('click', function(e){
        e.preventDefault();
        let LikeUrl = this.href;
        let LikeCounter = this.parentNode.children[0];
        let LikeDislike_Image = this.children[0];

        var xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function() {
            if (xhr.readyState === 4){
                let ResPosnse_LikeData = eval(xhr.responseText);
                if (ResPosnse_LikeData[0].liked === 'True'){
                    LikeCounter.innerHTML = `Like:${ResPosnse_LikeData[0].likes}`;
                    LikeDislike_Image.src = `/static/Icon/NormPro/IconForPosts/DisLikeIcon.svg`;

                }else if(ResPosnse_LikeData[0].liked === 'False'){
                    LikeCounter.innerHTML = `Like:${ResPosnse_LikeData[0].likes}`;
                    LikeDislike_Image.src = `/static/Icon/NormPro/IconForPosts/LikeIcon.svg`;
                }
            }
        };
        xhr.open('GET', LikeUrl);
        xhr.send()


    })
})