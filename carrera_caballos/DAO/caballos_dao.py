from utils.Conexion import get_mysql_conection
import utils.logging_carrera_caballos as log


class caballos_dao:
    _SELECCIONAR_INNERJOIN = "SELECT caballos.nombre,caballos.fecha_nacimiento,caballos.velocidad,caballos.experiencia,caballos.valor_apuesta,caballos.id_premio,gran_premio.nombre FROM caballos inner join gran_premio on caballos.id_premio = gran_premio.id WHERE caballos.id_premio = 1 order by gran_premio.id"
    _SELECCIONAR_INNERJOIN_2 = "SELECT caballos.nombre,caballos.fecha_nacimiento,caballos.velocidad,caballos.experiencia,caballos.valor_apuesta,caballos.id_premio,gran_premio.nombre FROM caballos inner join gran_premio on caballos.id_premio = gran_premio.id WHERE caballos.id_premio = 2 order by gran_premio.id"
    _SELECCIONAR = "SELECT * FROM caballos order by id"
    _INSERTAR = "INSERT INTO caballos(nombre, fecha_nacimiento, velocidad, experiencia, valor_apuesta,id_premio) VALUES(%s, %s, %s, %s, %s, %s)"
    _ACTUALIZAR = "UPDATE caballos SET experiencia=%s  WHERE id=%s"
    _ELIMINAR = "DELETE FROM caballos WHERE id=%s"

    @classmethod
    def seleccionar(cls):
        with get_mysql_conection() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(cls._SELECCIONAR)
                registros = cursor.fetchall()
                productos = []
                for registro in registros:
                    from POJO.clases_carrera_caballos import Caballo
                    caballo = Caballo(registro[1],registro[2],registro[3],registro[4],registro[5],registro[6])
                    productos.append(caballo)

                return productos

    @classmethod
    def seleccionar_id(cls):
        with get_mysql_conection() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(cls._SELECCIONAR)
                registros = cursor.fetchall()
                productos = []
                for registro in registros:
                    from POJO.clases_carrera_caballos import Caballo
                    caballo = Caballo(registro[0],registro[1],registro[2],registro[3],registro[4],registro[5])
                    productos.append(caballo)

                return productos
    @classmethod
    def insertar(cls, caballo):
        with get_mysql_conection() as conexion:
            with conexion.cursor() as cursor:
                print(caballo.fecha_nacimiento)
                valores = (caballo.nombre_caballo, caballo.fecha_nacimiento, caballo.velocidad, caballo.experiencia,caballo.valor_apuesta,caballo.id_caballo)
                cursor.execute(cls._INSERTAR, valores)
                conexion.commit()
                log.debug(f'productos insertada: {caballo}')
                return cursor.rowcount

    @classmethod
    def actualizar(cls, experiencia,valor_nuevo):
        with get_mysql_conection() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(cls._ACTUALIZAR, (experiencia,valor_nuevo))
                conexion.commit()
                registros_actualizados = cursor.rowcount
                log.debug(f'productos actualizada: {registros_actualizados}')

    @classmethod
    def eliminar(cls, producto):
        with get_mysql_conection() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(cls._ELIMINAR, producto.id)
                log.debug(f'Objeto eliminado: {producto}')
                return cursor.rowcount

    @classmethod
    def seleccionar_inner_join_gran_premio1(cls):
        with get_mysql_conection() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(cls._SELECCIONAR_INNERJOIN)
                registros = cursor.fetchall()
                productos = []
                for registro in registros:
                    from POJO.clases_carrera_caballos import Caballo
                    caballos = Caballo(registro[0],registro[1],registro[2],registro[3],registro[4],registro[5])
                    productos.append(caballos)
                return productos

    @classmethod
    def seleccionar_inner_join_gran_premio2(cls):
        with get_mysql_conection() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(cls._SELECCIONAR_INNERJOIN_2)
                registros = cursor.fetchall()
                productos = []
                for registro in registros:
                    from POJO.clases_carrera_caballos import Caballo
                    caballos = Caballo(registro[0], registro[1], registro[2], registro[3], registro[4], registro[5])
                    productos.append(caballos)
                return productos