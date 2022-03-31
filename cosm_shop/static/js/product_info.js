var check1 = document.querySelector('#op-1');
var check2 = document.querySelector('#op-2');
var text = document.querySelector('#text-info-prod');

function checkValue(about, compos) {
    console.log(about, compos)
    if (check1.checked) {
        text.innerText = about
        check2.checked = false
    } else {
        text.innerText = compos
        check2.checked = true
    }
}