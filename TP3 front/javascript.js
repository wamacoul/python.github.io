
var submit =document.getElementById("submit");
var toast = document.getElementById("toast-perso");
var textarea = document.getElementById("textarea");

let xhr =new XMLHttpRequest();
toast.style.display="none";

submit.addEventListener('click',validation);
function validation(e){
   if(textarea.validity.valueMissing){
        popup("mail manquant");
   }else{
    requete();
   }
}
function popup(message){
    toast.innerHTML=message
    toast.style.display="block";
    setTimeout(popupEnd,4000);
}
function popupEnd(){
    toast.style.display="none";
}
function requete(){
    xhr.open("GET",'http://127.0.0.1:8000/api/mail/?mail=\''+textarea.value+"'",true);
    xhr.send();
}
xhr.onload = function(){
    if(xhr.status !=200){
        popup("Erreur "+ xhr.status+ " : "+xhr.statusText);
    }else{
        popup("Votre Mail est un "+xhr.responseText);
    }
}