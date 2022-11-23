# This is a sample Python script.

# Press Alt+Mayús+X to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from abc import ABC, abstractmethod
import random
import utils.logging_orquesta as log
import utils.utils_afinaciones as afinacion
from Excepciones.Excepcion import AfinacionesException


def funcion_decorador_orquesta(funcion_a_decorar_b):
    def funcion_decorador_c(self):
        log.debug("Antes de la ejecución de la funcion")
        funcion_a_decorar_b(self)
        log.debug("Después de la ejecución de la funcion")

    return funcion_decorador_c


class Instrumento(ABC):
    def __init__(self,nombre_instrumento,tipo):
        self.__nombre_instrumento = nombre_instrumento
        self.__tipo = tipo
        self.__afinado = False

        # Atributo nombre

    @property
    def nombre(self):
        return self.__nombre_instrumento

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre_instrumento = nombre

    # Atributo tipo
    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo

    # Atributo afinado
    @property
    def afinado(self):
        return self._afinado

    @afinado.setter
    def afinado(self, afinado):
        self._afinado = afinado


    @abstractmethod
    def afinar(self):
        pass

    @abstractmethod
    def tocar(self):
        pass


class Guitarra(Instrumento):
    def __init__(self,nombre_instrumento,tipo,num_cuerdas):
        super().__init__(nombre_instrumento,tipo)
        self.num_cuerdas = num_cuerdas

    @property
    def num_cuerdas(self):
        return self._num_cuerdas

    @num_cuerdas.setter
    def num_cuerdas(self, num_cuerdas):
        self._num_cuerdas = num_cuerdas

    @funcion_decorador_orquesta
    def afinar(self):
        log.debug("Se esta comprobando si el instrumento esta bien afinado")
        aleatorio = random.choice(afinacion.AFINACIONES)
        if aleatorio:
            self.afinado = True
            log.debug("Guitarra ", self.nombre, " afinada correctamente")
        else:
            self.afinado = False
            log.debug("Guitarra ", self.nombre, " no afinada correctamente")

    @funcion_decorador_orquesta
    def tocar(self):
        if not self.afinar():
            raise AfinacionesException("No esta afinada la guitarra")
        else:
            log.debug("Tocando el instrumento ", self.nombre_instrumento, " de manera correcta")



class Guitarra_Electrica(Guitarra):
    def __init__(self,nombre_instrumento,tipo,num_cuerdas,potencia):
        super().__init__(nombre_instrumento, tipo,num_cuerdas)
        self.potencia = potencia

    @property
    def potencia(self):
        return self._potencia

    @potencia.setter
    def potencia(self, potencia):
        self._potencia = potencia

    @funcion_decorador_orquesta
    def afinar(self):
        log.debug("Se esta comprobando si el instrumento esta bien afinado")
        aleatorio = random.choice(afinacion.AFINACIONES)
        if aleatorio:
            self.afinado = True
            log.debug("Guitarra electrica ", self.nombre, " afinada correctamente")
        else:
            self.afinado = False
            log.debug("Guitarra electrica ", self.nombre, " no afinada correctamente")

    @funcion_decorador_orquesta
    def tocar(self):
        if not self.afinar():
            raise AfinacionesException("No esta afinada la guitarra")
        else:
            log.debug("Tocando el instrumento ", self.nombre_instrumento, " de manera correcta")

class Piano(Instrumento):
    def __init__(self,nombre_instrumento,tipo,num_teclas):
        super().__init__(nombre_instrumento, tipo)
        self._num_teclas = num_teclas

    @property
    def num_teclas(self):
        return self._num_teclas

    @num_teclas.setter
    def num_teclas(self, num_teclas):
        self._num_teclas = num_teclas


    @funcion_decorador_orquesta
    def afinar(self):
        log.debug("Se esta comprobando si el instrumento esta bien afinado")
        aleatorio = random.choice(afinacion.AFINACIONES)
        if aleatorio:
            self.afinado = True
            log.debug("Piano ", self.nombre, " afinado correctamente")
        else:
            self.afinado = False
            log.debug("Piano ", self.nombre, " no afinado correctamente")

    @funcion_decorador_orquesta
    def tocar(self):
        if not self.afinar():
            raise AfinacionesException("No esta afinada la guitarra")
        else:
            log.debug("Tocando el instrumento ", self.nombre_instrumento, " de manera correcta")

class Tambor(Instrumento):
    def __init__(self,nombre_instrumento,tipo, tamanio):
        super().__init__(nombre_instrumento, tipo)
        self._tamanio = tamanio

    @property
    def tamanio(self):
        return self._tamanio

    @tamanio.setter
    def num_cuerdas(self, tamanio):
        self._tamanio = tamanio


    @funcion_decorador_orquesta
    def afinar(self):
        log.debug("Se esta comprobando si el instrumento esta bien afinado")
        aleatorio = random.choice(afinacion.AFINACIONES)
        if aleatorio:
            self.afinado = True
            log.debug("Tambor ", self.nombre, " afinado correctamente")
        else:
            self.afinado = False
            log.debug("Tambor ", self.nombre, " no afinado correctamente")

    @funcion_decorador_orquesta
    def tocar(self):
        if  self.afinar():
            log.debug("Tocando el instrumento ", self.nombre_instrumento, " de manera correcta")
        else:
            raise AfinacionesException("No esta afinada la guitarra")

    def aporrear(self):
        log.debug("Aporreando el tamnbor ",self.nombre_instrumento)

class Orquesta:
    def __init__(self,nombre):
        self.nombre = nombre
        self.lista_instrumentos = []

    def crear_orquesta(self):
        guitarra = Guitarra("Guitarra","Española",8)
        guitarra_electrica1 = Guitarra_Electrica("Gitarra","electrica1",8, 1000)
        piano1 = Piano("Piano","Yamaha", 50)
        tambor1 = Tambor("Tambor1","Tipo", "Grande")
        self.lista_instrumentos = [guitarra, guitarra_electrica1,piano1,tambor1]



    def iniciar_concierto(self):
        self.afinar_instrumento()
        self.tocar_instrumento()

    def afinar_instrumento(self):
        for instrumento in self.lista_instrumentos:
            instrumento.afinar()

    def tocar_instrumento(self):
        log.debug("Tocando instrumentos..")
        try:
            for instrumento in self.lista_instrumentos:
                if isinstance(instrumento,Tambor):
                    instrumento.aporrear()
                else:
                    instrumento.tocar()
        except AfinacionesException as ine:
            log.debug(ine)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    orquesta1 = Orquesta("Mondragon")
    orquesta1.crear_orquesta()
    orquesta1.iniciar_concierto()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
