from utils.conexion import get_mysql_conection

try:
    conexion = get_mysql_conection()
    cursor = conexion.cursor()
    sentencia = 'SELECT nombre FROM Persona'
    cursor.execute(sentencia)
    registros = cursor.fetchall()
    print(registros)

except Exception as e:
    print("Error", e )
finally:
    cursor.close()
    conexion.close()
    print("Fin")