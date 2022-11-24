from utils.conexion import get_mysql_conection

try:
    conexion = get_mysql_conection()
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'UPDATE persona SET email=%s WHERE idPersonas=%s'
            valores = ('hectorfernandez@gmail.com', 1)
            valores1 = ('franciscohernandez@gmail.com', 3)
            cursor.execute(sentencia, valores)
            cursor.execute(sentencia, valores1)
            conexion.commit()
            registros_actualizados = cursor.rowcount
            print(f'Registros Actualizados: {registros_actualizados}')
except Exception as e:
    print(f'Ocurrió un error: {e}')