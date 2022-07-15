const peticion = new XMLHttpRequest()



function cargarMovimientos() {
    console.log('Has llamado a cargar movimientos')

    peticion.open('GET', 'http://127.0.0.1:5000/api/v1/movimientos', false)
    peticion.send()
    console.log(peticion.responseText)

    const tabla = document.querySelector('#cuerpo-tabla')
    const html = '<tr><td>05/01/2022</tr>';
    tabla.innerHTML += html;
}



window.onload = function () {
    const boton = document.querySelector('#boton-recarga')
    boton.addEventListener('click', cargarMovimientos)
};