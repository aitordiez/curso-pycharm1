
from utils.Conexion import get_mysql_conection
import utils.logging_carrera_caballos as log
class Apostantes_dao:

    _SELECCIONAR = "SELECT * FROM apostantes order by id"
    _INSERTAR = "INSERT INTO apostantes(nombre, saldo) VALUES(%s, %s)"
    _ACTUALIZAR = "UPDATE apostantes SET saldo=%s WHERE id=%s"
    _ELIMINAR = "DELETE FROM apostantes WHERE id=%s"

    @classmethod
    def seleccionar(cls):
        with get_mysql_conection() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(cls._SELECCIONAR)
                registros = cursor.fetchall()
                productos = []
                for registro in registros:
                    from POJO.clases_carrera_caballos import Apostante
                    apostantes = Apostante(registro[1],registro[2])
                    productos.append(apostantes)
                return productos

    @classmethod
    def seleccionar_id_apsotante(cls):
        with get_mysql_conection() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(cls._SELECCIONAR)
                registros = cursor.fetchall()
                productos = []
                for registro in registros:
                    from POJO.clases_carrera_caballos import Apostante
                    apostantes = Apostante(registro[0],registro[1], registro[2])
                    productos.append(apostantes)
                return productos

    @classmethod
    def insertar(cls, apostante):
        with get_mysql_conection() as conexion:
            with conexion.cursor() as cursor:
                valores = (apostante.nombre, apostante.saldo)
                cursor.execute(cls._INSERTAR, valores)
                conexion.commit()
                log.debug(f'productos insertada: {apostante}')
                return cursor.rowcount


    @classmethod
    def actualizar(cls, saldo,id_apostante):
        with get_mysql_conection() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(cls._ACTUALIZAR, (saldo,id_apostante))
                conexion.commit()
                registros_actualizados = cursor.rowcount
                log.debug(f'productos actualizada: {registros_actualizados}')

    @classmethod
    def eliminar(cls, apostante):
        with get_mysql_conection() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(cls._ELIMINAR, apostante.id)
                log.debug(f'Objeto eliminado: {apostante}')
                return cursor.rowcount