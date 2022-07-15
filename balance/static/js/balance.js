function cargarMovimientos() {
    console.log('Has llamado a cargar movimientos')
}


window.onload = function () {
    const boton = document.querySelector('#boton-recarga')
    boton.addEventListener('click', cargarMovimientos)
};