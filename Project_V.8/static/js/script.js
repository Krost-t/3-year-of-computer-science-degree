
var btn = document.getElementById("button");
btn.addEventListener("click",function () {
 
    if (btn.getAttribute("value") == "S'inscricre") {
        document.getElementById("switch-content").style.transform = 'translateX(400px)';
        btn.setAttribute("value","Connexion"); 
    }else if (btn.getAttribute("value") == "Connexion") {
        document.getElementById("switch-content").style.transform = 'translateX(0px)';
        btn.setAttribute("value","S'inscricre"); 
    }
   
});