function cargarMovimientos() {
    console.log('Has llamado a cargar movimientos')

    const tabla = document.querySelector('#cuerpo-tabla')
    const html = '<tr><td>05/01/2022</tr>';
    tabla.innerHTML = html;
}



window.onload = function () {
    const boton = document.querySelector('#boton-recarga')
    boton.addEventListener('click', cargarMovimientos)
};