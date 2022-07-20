var h1 = document.querySelector('h1');
function toggle(){
    if (h1.innerHTML === 'Hello!' )
        h1.innerHTML = 'Goodbye!';
    else h1.innerHTML = 'Hello!';
}
document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('button').onclick = toggle;
});