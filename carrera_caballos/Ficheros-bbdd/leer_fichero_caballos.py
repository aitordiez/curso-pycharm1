#import DAO.caballos_dao as dao
from POJO.clases_carrera_caballos import Caballo
if __name__ == "__main__":
    archivo = open("C:/Users/Aitor Diez/PycharmProjects/carrera_caballos/Ficheros/caballos.txt","r",encoding="UTF-8")
    for datos_leer in archivo.readlines():
        datos = datos_leer.split("|")
        caballos = Caballo(datos[0],datos[1],datos[2],datos[3],datos[4],datos[5])
        #dao.caballos_dao.insertar(caballos)