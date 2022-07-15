from flask import jsonify, render_template, request
from . import app
from .models import DBManager

"""
Verbos y formato de endpoints
------------------------------
GET /movimientos ---> LISTA movimientos
POST /movimientos ---> CREAR movimiento
GET /movimientos/1 --> LEER el movimiento con ID 1
POST /movimientos/1 -> ACTUALIZAR el movimiento con ID 1 (sobreescribe todo el objeto)
PUT /movimientos/1 --> ACTUALIZAR el movimiento con ID 1 (sobreescribe parcialmente)
DELETE /movimientos/1 -> ELIMINAR el movimiento con ID 1

importante versionar los endpoints (son un contrato)
/apo/v1/...
"""

RUTA = app.config.get("RUTA")
db = DBManager(RUTA)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/v1/movimientos")
def listar_movimientos():
    try:
        sql = "SELECT * from movimientos ORDER BY fecha, id"
        movimientos = db.consultaSQL(sql)
        if movimientos:
            resultado = {"status": "success", "results": movimientos}
            status_code = 200
        else:
            resultado = {"status": "error", "message": "No hay movimientos"}
    except Exception as error:
        resultado = {
            "status": "error",
            "message": str(error)
        }
        status_code = 503
    return jsonify(resultado), status_code


@app.route("/api/v1/movimientos", methods=["POST"])
def insertar_movimiento():
    try:
        sql = ("INSERT INTO movimientos (fecha,concepto,tipo,cantidad)"
               "VALUES (:fecha, :concepto, :tipo, :cantidad)")
        db = DBManager(RUTA)
        ha_ido_bien = db.consultaConParametros(sql, request.json)
        if ha_ido_bien:
            resultado = {"status": "success"}
            status_code = 201
        else:
            resultado = {
                "status": "error",
                "message": "Error al insertar el movimiento en la base de datos"}
            status_code = 503
    except Exception as error:
        resultado = {
            "status": "error",
            "message": str(error)
        }
        status_code = 404
    return jsonify(resultado)


@app.route("/api/v1/movimientos/<int:id>")
def obtener_movimiento_por_id(id):
    movimiento = db.obtenerMovimientoPorId(id)
    if movimiento:
        resultado = {"status": "success", "results": movimiento}
        status_code = 200
    else:
        resultado = {
            "status": "error",
            "message": f"No he encontrado el movimiento con id {id}"
        }
        status_code = 404
    return jsonify(resultado), status_code


@app.route("/api/v1/movimientos/<int:id>", methods=['DELETE'])
def eliminar_movimiento_por_id(id):
        sql = "DELETE FROM movimientos WHERE id=?"
        params = (id,)
        ha_ido_bien = db.consultaConParametros(sql, params)
        if ha_ido_bien:
            status_code = 204
            return jsonify({"status": "success"}), status_code
        else:
            status_code = 500
            return jsonify(
                {"status": "error", "message": f"Ha fallado el borrado del movimiento {id}"}
                ), status_code
            
    


@app.route("/api/v1/movimientos/<int:id>", methods=['POST'])
def actualizar_movimiento_por_id(id):
    try:
        sql = "UPDATE movimientos SET {fecha,concepto,tipo,cantidad} where id=?"
        "VALUES(:fecha , :concepto , :tipo , :cantidad)"
        params = [id]
        diccionario = request.json
        for elem in diccionario:
            params.append(diccionario[elem])
        params = tuple(params)
        ha_ido_bien = db.consultaConParametros(sql, params)
        if ha_ido_bien:
            resultado = {"status": "success"}
        else:
            resultado = {
                "status": "error",
                "message": "Error al modificar el movimiento en la base de datos"}
    except Exception as error:
        resultado = {
            "status": "error",
            "message": str(error)
        }
    return jsonify(resultado)
