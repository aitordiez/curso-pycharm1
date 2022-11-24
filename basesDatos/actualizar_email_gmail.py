from utils.conexion import get_mysql_conection

try:
    conexion = get_mysql_conection()
    with conexion:
        with conexion.cursor() as cursor:
            sentencia_select = "SELECT idPersonas FROM persona WHERE email NOT LIKE '%gmail.com%'"
            resultado = cursor.execute(sentencia_select)
            registros = cursor.fetchall()
            print(registros)
            sentencia = "UPDATE persona SET email=%s WHERE idPersonas=%s"
            valores = ('hectorfernandez@gmail.com',registros[0])
            valores1 = ('franciscohernandez@gmail.com',registros[1])
            cursor.execute(sentencia, valores)
            cursor.execute(sentencia, valores1)
            conexion.commit()
            registros_actualizados = cursor.rowcount
            print(f'Registros Actualizados: {registros_actualizados}')
except Exception as e:
    print(f'Ocurrió un error: {e}')