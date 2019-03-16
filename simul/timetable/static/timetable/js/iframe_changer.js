function arrow_switch(){
    var up= document.getElementById('up_arrow');
    var down= document.getElementById('down_arrow');
    if up.style.visibility==="visible"{
        up.style.visibility='hidden';
        down.style.visibility='visible';
    }
    else{
        down.style.visibility='hidden';
        up.style.visibility='visible';   
    }
}