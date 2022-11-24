# This is a sample Python script.

# Press Alt+Mayús+X to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import utils.logging_archivos as log
from Excepcion.excepciones import ArchivoException

class Colegio:

    def __init__(self,nombre_colegio):
        self.__nombre_colegio = nombre_colegio

    @property
    def nombre_colegio(self):
        return self.__nombre_colegio

    @nombre_colegio.setter
    def nombre_colegio(self,nombre_colegio):
        self.__nombre_colegio = nombre_colegio


    def recoger_datos(self):
        colegios_alumno = []
        try:
            log.debug("Se abre el archivo")
            archivo_leer = open("./Archivo/alumnos-colegio.txt","r",encoding="UTF-8")
            for leer in archivo_leer.readlines():
                log.debug("lineas que contiene el archivo ",leer)
                datos = leer.split("|;")
                colegios_alumno = [datos]
                print(colegios_alumno)
                if leer.split("|") and leer.split(";"):
                    log.debug("Abrimos los archivos donde se van a añadir las lineas")
                    archivo_escribir = open("./Archivo/"+self.nombre_colegio+".txt","a",encoding="UTF-8")
                    log.debug("Escribimos las lineas ",leer, " en cada fichero que corresponda ",archivo_escribir)
                    archivo_escribir.write(leer)
        except ArchivoException as e:
            log.error("Excepcion", e)
        finally:
            archivo_escribir.close()
            archivo_leer.close()
            log.debug("cerramos los archivos ")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    log.debug("Empezando...")
    colegio1 = Colegio("Colegio1")
    colegio1.recoger_datos()
    colegio2 = Colegio("Colegio2")
    colegio2.recoger_datos()
    colegio3 = Colegio("Colegio3")
    colegio3.recoger_datos()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
