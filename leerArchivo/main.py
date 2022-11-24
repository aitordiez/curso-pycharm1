# This is a sample Python script.

# Press Alt+Mayús+X to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import utils.logging_archivos as log
from Excepcion.excepciones import ArchivoException
class Alumno:
    def __init__(self, nombre, apellidos, dni, asignaturas):
        self._nombre = nombre
        self._apellidos = apellidos
        self._dni = dni
        self._asignaturas = asignaturas

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellidos(self):
        return self._apellidos

    @apellidos.setter
    def apellidos(self, apellidos):
        self._apellidos = apellidos

    @property
    def dni(self):
        return self._dni

    @dni.setter
    def dni(self, dni):
        self._dni = dni

    @property
    def asignaturas(self):
        return self._asignaturas

    @asignaturas.setter
    def asignaturas(self, asignaturas):
        self._asignaturas = asignaturas

    def addAsignatura(self, asignatura):
        self.asignaturas.append(asignatura)

    def __str__(self):
        return f"{self.nombre}|{self.apellidos}|{self.dni}|"+";".join(self.asignaturas)

class Colegio:

    def __init__(self,nombre_colegio):
        self.__nombre_colegio = nombre_colegio
        self.lista_alumnos = []

    @property
    def nombre_colegio(self):
        return self.__nombre_colegio

    @nombre_colegio.setter
    def nombre_colegio(self,nombre_colegio):
        self.__nombre_colegio = nombre_colegio


    def recoger_datos(self):
        log.debug("Se abre el archivo")
        archivo_leer = open("./Archivo/alumnos-colegio.txt","r",encoding="UTF-8")
        for leer in archivo_leer.readlines():
           log.debug("lineas que contiene el archivo ",leer)
           datos = leer.split("|")
           if not datos[0].find(self.nombre_colegio):
            alumno = Alumno(datos[1],datos[2],datos[3],datos[4].split(";"))
            archivo_escribir = open("./Archivo/" + self.nombre_colegio + ".txt", "a", encoding="UTF-8")
            archivo_escribir.write(str(alumno))
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
