$(function(){

    $('#id_rut').keypress(function(e) {
      if(isNaN(this.value + String.fromCharCode(e.charCode))) 
        return false;
       if(String.fromCharCode(e.charCode) == "."){
        return false;
       }
    })
    .on("cut copy paste",function(e){
      e.preventDefault();
    });
  
  });

document.getElementById("id_rut").oninput = function(){
    var evento_key = window.KeyboardEvent
    console.log(evento_key)
}