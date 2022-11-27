from utils.Conexion import get_mysql_conection
import utils.logging_carrera_caballos as log
class gran_premio_dao:

    _SELECCIONAR = "SELECT * FROM gran_premio order by id"
    _INSERTAR = "INSERT INTO gran_premio(nombre, distancia, num_carreras) VALUES(%s, %s, %s)"
    _ACTUALIZAR = "UPDATE gran_premio SET nombre=%s, distancia=%s, num_carreras=%s WHERE id=%s"
    _ELIMINAR = "DELETE FROM gran_premio WHERE id=%s"

    @classmethod
    def seleccionar(cls):
        with get_mysql_conection() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(cls._SELECCIONAR)
                registros = cursor.fetchall()
                productos = []
                for registro in registros:
                    from POJO.clases_carrera_caballos import Gran_premio
                    premio = Gran_premio(registro[1], registro[2], registro[3])
                    productos.append(premio)

                return productos

    @classmethod
    def insertar(cls, gran_premio):
        with get_mysql_conection() as conexion:
            with conexion.cursor() as cursor:
                valores = (gran_premio.nombre_premio, gran_premio.distancia, gran_premio.num_carreras)
                cursor.execute(cls._INSERTAR, valores)
                conexion.commit()
                log.debug(f'productos insertada: {gran_premio}')
                return cursor.rowcount

    @classmethod
    def actualizar(cls, gran_premio):
        with get_mysql_conection() as conexion:
            with conexion.cursor() as cursor:
                valores = (gran_premio.nombre_premio, gran_premio.distancia, gran_premio.num_carreras)
                cursor.execute(cls._ACTUALIZAR, valores)
                log.debug(f'productos actualizada: {gran_premio}')
                return cursor.rowcount

    @classmethod
    def eliminar(cls, gran_premio):
        with get_mysql_conection() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(cls._ELIMINAR, gran_premio.id)
                log.debug(f'Objeto eliminado: {gran_premio}')
                return cursor.rowcount