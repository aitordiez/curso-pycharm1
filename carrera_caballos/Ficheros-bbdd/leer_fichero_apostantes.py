import utils.logging_carrera_caballos as log
import DAO.apostantes_dao as dao
from POJO.clases_carrera_caballos import *
if __name__ == "__main__":
    archivo = open("C:/Users/Aitor Diez/PycharmProjects/carrera_caballos/Ficheros/apostantes.txt","r",encoding="UTF-8")
    for datos_leer in archivo.readlines():
        datos = datos_leer.split("|")
        apostante = Apostante(datos[0],datos[1])
        dao.apostantes_dao.insertar(apostante)
