


var modal = document.getElementsByClassName("modal");

for(var i=0; i<modal.length; i++) { 

    var lmodal = modal[i]
}

var modalImg = document.getElementsByClassName("img01");

for(var i=0; i<modalImg.length; i++) { 

var lmoalImg = modalImg[i]
}





var img = document.getElementsByClassName("geeks");


for(i=0;i<img.length;i++){
    img[i].onclick = function () {
        lmodal.style.display = "block";
        lmoalImg.src = this.src;
    }

   
    
}



var span = document.getElementsByClassName("close");

for(i=0;i<span.length;i++){
    span[i].onclick = function () {
    lmodal.style.display = "none";
}
}

