let spinner;
const peticion = new XMLHttpRequest();

function obtenerMovimientos() {
    spinner.classList.remove('off');
    console.log("Obteniendo movimientos");
    peticion.open('GET', 'http://127.0.0.1:5000/api/v1/movimientos', true);
    peticion.send();
    console.log("FIN de obtener movimientos");
}

function mostrarMovimientos() {
    console.log('entramos en mostrar movimientos');
    const tabla = document.querySelector('#cuerpo-tabla');

    if (this.readyState === 4 && this.status === 200) {
        console.log('--- TODO OK ----');
        const respuesta = JSON.parse(peticion.responseText);
        const movimientos = respuesta.results;


        let html = '';
        for (let i = 0; i < movimientos.length; i = i + 1) {
            const mov = movimientos[i];
            if (mov.tipo === 'G') {
                mov.tipo = 'Gasto';
            } else if (mov.tipo === 'I') {
                mov.tipo = 'Ingreso';
            } else {
                mov.tipo = '---';
            }
            html = html + `
        <tr>
          <td>${mov.fecha}</td>
          <td>${mov.concepto}</td>
          <td>${mov.tipo}</td>
          <td>${mov.cantidad}</td>
        </tr>
      `;
        }

        tabla.innerHTML = html;
    } else {
        console.error('---- Algo ha ido mal en la petición ----');
        alert('Error al cargar los movimientos');
    }
    console.log('FIN de mostrar movimientos');
    spinner.classList.add('off');
}

window.onload = function () {
    spinner = document.querySelector('#spinner');
    console.log('Inicio de window.onload');
    obtenerMovimientos();
    peticion.onload = mostrarMovimientos;

    const boton = document.querySelector('#boton-recarga');
    boton.addEventListener('click', obtenerMovimientos);
};