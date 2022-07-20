let person = {
    first: 'Harry',
    last: 'Potter'
};

function mostrar() {
    document.querySelector('#nombre').innerHTML = person['first'];
    document.querySelector('#apellido').innerHTML = person.last;
}

document.querySelector('button').onclick = mostrar;