import utils.logging_carrera_caballos as log
import DAO.gran_premio_dao as dao
from POJO.clases_carrera_caballos import Gran_premio
if __name__ == "__main__":
    archivo = open("C:/Users/Aitor Diez/PycharmProjects/carrera_caballos/Ficheros/grandes_premios.txt","r",encoding="UTF-8")
    for datos_leer in archivo.readlines():
        datos = datos_leer.split("|")
        gran_premio = Gran_premio(datos[0],datos[1],datos[2])
        dao.gran_premio_dao.insertar(gran_premio)