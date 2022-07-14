import sqlite3


class DBManager:
    def __init__(self, ruta):
        self.ruta = ruta

    def consultaSQL(self, consulta):
        # 1- Conectar con la base de datos
        conexion = sqlite3.connect(self.ruta)

        # 2- Generar un cursor para recorrer el resultado de la consulta
        cursor = conexion.cursor()

        # 3- Pasarle la consulta SQL a ejecutar y ejecutarla
        cursor.execute(consulta)

        # 4- Tratar los datos
        #   4.1 - Obtener los nombres de columna

        #   4.2 - Pedir todos los datos (registros)
        #   4.3 - Recorrer los resultados:
        #       4.3.1 - Crear un diccionario
        #           - Recorrer la lista de los nombres de columna
        #           - Para cada columna: nombre + valor
        #       4.3.2 - Guardar en la lista de movimientos
        # [{'nombre_col1': {valor_col1, ...}]

        self.movimientos = []
        nombres_columnas = []

        for desc_columna in cursor.description:
            nombres_columnas.append(desc_columna[0])
        # nombre_columnas = ['nom_col1','nom_col2'...]
        # nombres_columnas = ['id','fecha','concepto','tipo','cantidad']

        datos = cursor.fetchall()
        for dato in datos:
            movimiento = {}
            indice = 0
            for nombre in nombres_columnas:
                movimiento[nombre] = dato[indice]
                indice += 1
            self.movimientos.append(movimiento)

        conexion.close()

        return self.movimientos

    def obtenerMovimientoPorId(self, id):
        consulta = "SELECT * FROM movimientos WHERE id=?"
        conexion = sqlite3.connect(self.ruta)
        cursor = conexion.cursor()
        cursor.execute(consulta,(id,))
        
        datos = cursor.fetchone()
        resultado = None

        if datos:
            nombres_columnas = []
            for desc_columna in cursor.description:
                nombres_columnas.append(desc_columna[0])
            movimiento = {}
            indice = 0
            for nombre in nombres_columnas:
                movimiento[nombre] = datos[indice]
                indice += 1
            resultado = movimiento

        conexion.close()
        return resultado

    def consultaConParametros(self,consulta,params):
        conexion = sqlite3.connect(self.ruta)
        cursor = conexion.cursor()
        resultado = False
        try:
            cursor.execute(consulta,params)
            conexion.commit()
            resultado = True
        except Exception as error:
            print("ERROR DB:", error)
            conexion.rollback()
        conexion.close()
        return resultado

    
        