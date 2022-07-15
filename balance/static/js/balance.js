const peticion = new XMLHttpRequest()



function cargarMovimientos() {
    console.log('Has llamado a cargar movimientos')

    peticion.open('GET', 'http://127.0.0.1:5000/api/v1/movimientos', false)
    peticion.send()
    const respuesta = JSON.parse(peticion.responseText)
    const movimientos = respuesta.results;

    const tabla = document.querySelector('#cuerpo-tabla')
    let html = '';
    for (let i = 0; i < movimientos.length; i= i+1) {
        const mov = movimientos[i]
        html = html + `
        <tr>
            <td>${mov.fecha}</td>
            <td>${mov.concepto}</td>
            <td>${mov.tipo}</td>
            <td>${mov.cantidad}</td>
        </tr>
        `

    } 
    tabla.innerHTML = html;
}



window.onload = function () {
    const boton = document.querySelector('#boton-recarga')
    boton.addEventListener('click', cargarMovimientos);
    cargarMovimientos();
};