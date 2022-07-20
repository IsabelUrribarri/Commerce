var toggleCheck = function () {
    let parent = this.parentNode;
    parent.classList.toggle('checked');
}
var deleteTask = function () {
    let li = this.parentNode;
    let parent = li.parentNode;
    parent.removeChild(li);
}
var createTodo = function (todo) {
    //crear input checkbox
    var checkbox = document.createElement('input');
    checkbox.setAttribute('type', 'checkbox');
    //crear label
    var label = document.createElement('label');
    //crear boton delete
    var boton = document.createElement('button');
    boton.innerHTML = 'Delete';
    boton.classList.add('delete');
    var li = document.createElement('li');

    var ul = document.querySelector('ul');
    ul.appendChild(li);
    var tarea_nueva = document.getElementById('newTodo');
    console.log(tarea_nueva);
    label.innerHTML = tarea_nueva.value;
    li.appendChild(checkbox);
    li.appendChild(label);
    li.appendChild(boton);
    checkbox.onclick = toggleCheck;
    boton.onclick = deleteTask;

    return li
}
var boton_agregar = document.getElementsByClassName('add');
boton_agregar.onclick = function () {
    var ul = document.querySelector('ul');
    var tarea_nueva = document.getElementById('newTodo');
    if (tarea_nueva.value !== "") {
        var li = createTodo(tarea_nueva.value);
        ul.appendChild(li);
        tarea_nueva.value = "";
    }

}
document.getElementById('newTodo').onkeydown = enterKey;
function enterKey(e) {
    if (e.code === "Enter") boton_agregar.onclick();
}