var select = document.getElementById('cream')
var button = document.querySelector("button");
button.addEventListener("click", function() {
    if (select.checked){
        console.log(select.id);
    } else {
        console.log(select.checked);}
});


