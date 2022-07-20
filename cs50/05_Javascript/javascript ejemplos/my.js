
cont = 0;
var h1 = document.querySelector('h1');
function click() {
    cont++
    h1.innerHTML = cont
}
document.addEventListener('DOMContentLoaded', function () {
    document.querySelector('button').onclick = click;
});
