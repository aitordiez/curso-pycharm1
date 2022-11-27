import utils.logging_carrera_caballos as log
# Abstract Basic Class
from abc import ABC, abstractmethod
import DAO.caballos_dao as dao_caballos
import DAO.apostantes_dao as dao_apostantes
import DAO.gran_premio_dao as dao_gran_premio
from datetime import datetime
from utils.general_utils import pide_datos
import random


class Persona(ABC):
    def __init__(self,nombre):
        self._nombre = nombre

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self,nombre):
        self._nombre = nombre

    def __str__(self):
        return f"{self.nombre}"

class Apostante:
    def __init__(self,id_apostante,nombre,saldo):
        self._id_apostante = id_apostante
        self._saldo = saldo
        self._nombre = nombre

    @property
    def id_apostante(self):
        return self._id_apostante

    @id_apostante.setter
    def id_apostante(self, id_apostante):
        self._id_apostante = id_apostante

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self,saldo):
        self._saldo = saldo

    def pedir_apuesta_apostante1(self):
        registro_nombre_apostante = dao_apostantes.Apostantes_dao.seleccionar_id_apsotante()
        registro_nombre_caballos = dao_caballos.caballos_dao.seleccionar()
        resultado = pide_datos("Introduce la apuesta que desee realizar")
        apostante1 = registro_nombre_apostante[0]
        caballos1 = registro_nombre_caballos[0]
        saldo = apostante1.saldo - resultado
        id_apostante = apostante1.id_apostante
        if saldo > 0 and saldo <= apostante1.saldo:
            actualizar_datos = dao_apostantes.Apostantes_dao.actualizar(saldo,id_apostante)
        else:
            print("No se podria hacer una apuesta")
            pide_datos("Introduzca de nuevo la apuesta")





    def resumen_apuesta_apostante(self):
        registro_apuestas_apostante = dao_apostantes.Apostantes_dao.seleccionar()
        for apuestas_apostante in registro_apuestas_apostante:
            print(apuestas_apostante.saldo)


class Caballo:
    def __init__(self,nombre_caballo,fecha_nacimiento,velocidad,experiencia,valor_apuesta,id_caballo):
        self._nombre_caballo = nombre_caballo
        self._fecha_nacimiento = fecha_nacimiento
        self._velocidad = velocidad
        self._experiencia = experiencia
        self._valor_apuesta = valor_apuesta
        self._id_caballo = id_caballo
        self._array_valores_caballo1 = []
        self._array_valores_caballo2 = []
        self._array_valores_caballo3 = []

    @property
    def valores(self):
        return self._array_valores_caballo1

    @valores.setter
    def array_valores(self, array_valores_caballo1):
            self._array_valores_caballo1 = array_valores_caballo1

    def addAlumno(self, array_valores_caballo1):
        self.array_valores.append(array_valores_caballo1)

    @property
    def valores_caballo2(self):
        return self._array_valores_caballo2

    @valores_caballo2.setter
    def array_valores_caballo2(self, valores_caballo2):
        self._array_valores_caballo2 = valores_caballo2

    def addAlumno(self, array_valores_caballo2):
        self.array_valores_caballo2.append(array_valores_caballo2)

    @property
    def valores_caballo3(self):
        return self._array_valores_caballo3

    @valores_caballo3.setter
    def array_valores_caballo3(self, array_valores_caballo3):
        self._array_valores_caballo3 = array_valores_caballo3

    def addAlumno(self, array_valores_caballo3):
        self.array_valores_caballo3.append(array_valores_caballo3)
    @property
    def nombre_caballo(self):
        return self._nombre_caballo

    @nombre_caballo.setter
    def nombre_caballo(self,nombre_caballo):
        self._nombre_caballo = nombre_caballo

    @property
    def fecha_nacimiento(self):
        return self._fecha_nacimiento

    @fecha_nacimiento.setter
    def fecha_nacimiento(self,fecha_nacimiento):
        self._fecha_nacimiento = fecha_nacimiento

    @property
    def velocidad(self):
        return self._velocidad

    @velocidad.setter
    def velocidad(self,velocidad):
        self._velocidad = velocidad

    @property
    def experiencia(self):
        return self._experiencia

    @experiencia.setter
    def experiencia(self,experiencia):
        self._experiencia = experiencia

    @property
    def valor_apuesta(self):
        return self._valor_apuesta

    @valor_apuesta.setter
    def valor_apuesta(self,valor_apuesta):
        self._valor_apuesta = valor_apuesta

    @property
    def id_caballo(self):
        return self._id_caballo

    @id_caballo.setter
    def id_caballo(self, id_caballo):
        self._id_caballo = id_caballo

    def __str__(self):
        return f"{self.nombre_caballo}|{self.fecha_nacimiento}|{self.experiencia}|{self.velocidad}|{self.valor_apuesta}|{self.id_caballo}"

    def correr(self):
        print("Los nombres de los caballos que corren ",self.nombre_caballo)

    def mostrar_caballo_valor_apuesta(self):
        registro_caballos_corren = dao_caballos.caballos_dao.seleccionar_inner_join_gran_premio1()
        for caballos_corren in registro_caballos_corren:
            print("El nombre del caballo es: ", caballos_corren.nombre_caballo, " y su valor de apuesta es: ",caballos_corren.valor_apuesta)

    def mostrar_caballo_valor_apuesta2(self):
        registro_caballos_corren = dao_caballos.caballos_dao.seleccionar_inner_join_gran_premio2()
        for caballos_corren in registro_caballos_corren:
            print("El nombre del caballo es: ", caballos_corren.nombre_caballo, " y su valor de apuesta es: ",caballos_corren.valor_apuesta)
    def recuperar_valor_apuesta(self):
        recoger_valor_apuesta = []
        registro_caballos_valor_apuesta = dao_caballos.caballos_dao.seleccionar()
        for registro_valor_apuesta in registro_caballos_valor_apuesta:
            recoger_valor_apuesta.append(registro_valor_apuesta.valor_apuesta)

        return recoger_valor_apuesta

    def preguntar_valor_apuesta(self):
        array_datos_valor_apuesta = self.recuperar_valor_apuesta()
        valor_apuesta_apostante = pide_datos("Introduce el valor de apuesta del caballo")


    def calcular_anho_caballo(self):
        registro_caballos=dao_caballos.caballos_dao.seleccionar()
        for registro in registro_caballos:
            datos = registro.fecha_nacimiento
            resultado = str(datos)
            fecha = datetime.strptime(resultado,"%Y-%m-%d")
            anho = fecha.year
            fecha_actual = datetime.now()
            resultado_edad = fecha_actual.year -anho
            return resultado_edad

    def generar_numero_aleatorio(self):
        aleatorio = random.randint(1,50)
        print(aleatorio)
        return aleatorio

    def caballo_ganador_gran_premio1(self):
        recoger_datos_distancia = dao_gran_premio.gran_premio_dao.seleccionar()
        recoger_distancia = recoger_datos_distancia[0]
        distancia = int(recoger_distancia.distancia)
        return distancia
    def avanzar_caballos(self):
        ganar_caballo1 = False
        resultado = 0
        recoger_datos_caballos = dao_caballos.caballos_dao.seleccionar()
        distancia_gran_premio = self.caballo_ganador_gran_premio1()
        recoger_datos_caballo1 = recoger_datos_caballos[0]
        avanza_caballo1 = recoger_datos_caballo1.velocidad + recoger_datos_caballo1.experiencia - recoger_datos_caballo1.calcular_anho_caballo() + recoger_datos_caballo1.generar_numero_aleatorio()
        self.array_valores.append(avanza_caballo1)
        if len(self.array_valores) > 1:
            for resultado_total in self.array_valores:
                resultado += resultado_total
            if resultado >= distancia_gran_premio:
                experiencia = recoger_datos_caballo1.experiencia + 5
                print(experiencia)
                recoger_datos_caballos_id_ganador = dao_caballos.caballos_dao.seleccionar_id()
                recoger_datos_id_caballo = recoger_datos_caballos_id_ganador[0]
                recoger_id_caballo = recoger_datos_id_caballo.nombre_caballo
                print(recoger_id_caballo)
                ganar_caballo1 = True
                recoger_datos_experiencia_caballo1 = dao_caballos.caballos_dao.actualizar(experiencia,recoger_id_caballo)
        return ganar_caballo1
    def avanzar_caballos2(self):
        ganar_caballo2 = False
        resultado_distancia_caballo2 = 0
        recoger_datos_caballos = dao_caballos.caballos_dao.seleccionar()
        distancia_gran_premio = self.caballo_ganador_gran_premio1()
        recoger_datos_caballo2 = recoger_datos_caballos[1]
        avanza_caballo2 = recoger_datos_caballo2.velocidad + recoger_datos_caballo2.experiencia - recoger_datos_caballo2.calcular_anho_caballo() + recoger_datos_caballo2.generar_numero_aleatorio()
        self.array_valores_caballo2.append(avanza_caballo2)
        if len(self.array_valores_caballo2) > 1:
            for resultado_total in self.array_valores_caballo2:
                resultado_distancia_caballo2 += resultado_total
            if resultado_distancia_caballo2 >= distancia_gran_premio:
                experiencia = recoger_datos_caballo2.experiencia + 5
                print(experiencia)
                recoger_datos_caballos_id_ganador = dao_caballos.caballos_dao.seleccionar_id()
                recoger_datos_id_caballo = recoger_datos_caballos_id_ganador[1]
                recoger_id_caballo = recoger_datos_id_caballo.nombre_caballo
                print(recoger_id_caballo)
                ganar_caballo2 = True
                recoger_datos_experiencia_caballo2 = dao_caballos.caballos_dao.actualizar(experiencia,recoger_id_caballo)
        return ganar_caballo2

    def avanzar_caballos3(self):
        ganar_caballo3 = False
        resultado_distancia_caballo3 = 0
        recoger_datos_caballos = dao_caballos.caballos_dao.seleccionar()
        distancia_gran_premio = self.caballo_ganador_gran_premio1()
        recoger_datos_caballo3 = recoger_datos_caballos[2]
        avanza_caballo3 = recoger_datos_caballo3.velocidad + recoger_datos_caballo3.experiencia - recoger_datos_caballo3.calcular_anho_caballo() + recoger_datos_caballo3.generar_numero_aleatorio()
        self.array_valores_caballo3.append(avanza_caballo3)
        if len(self.array_valores_caballo3) > 1:
            for resultado_total in self.array_valores_caballo3:
                resultado_distancia_caballo3 += resultado_total
            if resultado_distancia_caballo3 >= distancia_gran_premio:
                ganar_caballo3 = True

        return ganar_caballo3

    def caballo_corriendo_gran_premio(self):
        resultado = dao_caballos.caballos_dao.seleccionar_inner_join()
        print(resultado)

    def caballo_perdedor_gran_premio(self):
        recoger_datos_experiencia = dao_caballos.caballos_dao.seleccionar()
        for datos_recogidos in recoger_datos_experiencia:
            print(datos_recogidos.experiencia)
class Gran_premio:
    def __init__(self,nombre_premio,distancia,num_carreras):
        self._nombre_premio = nombre_premio
        self._distancia = distancia
        self._num_carreras = num_carreras

    @property
    def nombre_premio(self):
        return self._nombre_premio

    @nombre_premio.setter
    def nombre_premio(self,nombre_premio):
        self._nombre_premio = nombre_premio

    @property
    def distancia(self):
        return self._distancia

    @distancia.setter
    def distancia(self,distancia):
        self._distancia = distancia

    @property
    def num_carreras(self):
        return self._num_carreras

    @num_carreras.setter
    def num_carreras(self,num_carreras):
        self._num_carreras = num_carreras

    def __str__(self):
        return f"{self.nombre_premio}|{self.distancia}|{self.num_carreras}"

    def mostrar_gran_premios(self):
        recoger_datos_gran_premio = dao_gran_premio.gran_premio_dao.seleccionar()
        for recoger_datos in recoger_datos_gran_premio:
            print("el nombre del gran premio es ", recoger_datos.nombre_premio, " las vueltas son: ",recoger_datos.num_carreras)






