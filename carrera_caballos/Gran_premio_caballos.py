# This is a sample Python script.

# Press Alt+Mayús+X to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from utils.general_utils import pide_datos
from POJO.clases_carrera_caballos import Apostante,Caballo,Gran_premio
import DAO.gran_premio_dao as dao_gran_premio
import DAO.caballos_dao as dao_caballos
# Press the green button in the gutter to run the script.
def pide_menu(menu=None):
    if menu == None:
        print("1.Gran premio 1\n2.Gran premio 2\n3.Salir\n")
        return pide_datos(menu, "int")

if __name__ == '__main__':
    caballo = Caballo("Paco","2020-12-03",20,30,5,1)
    apuesta = Apostante(8,"Aitor",200)
    salir = False
    opcion = 0
    while not salir:
        opcion = pide_menu()
        if opcion == 1:
            numero_vueltas = 0
            print("Has seleccionado el gran premio 1")
            resultado = apuesta.pedir_apuesta_apostante1()

            recoger_datos_gran_premio1 = dao_gran_premio.gran_premio_dao.seleccionar()
            recoger_datos_caballos1 = dao_caballos.caballos_dao.seleccionar()
            caballo.mostrar_caballo_valor_apuesta()
            resultado_apuesta = pide_datos("Introduce el valor de la apuesta del caballo")
            recoger_Datos_caballos = recoger_datos_caballos1[0]
            valor_apuesta1 = recoger_Datos_caballos.valor_apuesta
            recoger_Datos_caballos2 = recoger_datos_caballos1[1]
            valor_apuesta2 = recoger_Datos_caballos2.valor_apuesta
            recoger_Datos_caballos3 = recoger_datos_caballos1[2]
            valor_apuesta3 = recoger_Datos_caballos3.valor_apuesta
            recoger_datos = recoger_datos_gran_premio1[0]

            numero_carreras = int(recoger_datos.num_carreras)
            while numero_vueltas < numero_carreras:
                resultado_caballo1 = caballo.avanzar_caballos()
                resultado_caballo2 = caballo.avanzar_caballos2()
                resultado_caballo3 = caballo.avanzar_caballos3()
                numero_vueltas+=1

        elif opcion == 2:
            print("Has seleccionado el gran premio 2")
            numero_vueltas = 0
            resultado = apuesta.pedir_apuesta_apostante1()

            recoger_datos_gran_premio1 = dao_gran_premio.gran_premio_dao.seleccionar()
            recoger_datos_caballos1 = dao_caballos.caballos_dao.seleccionar()
            caballo.mostrar_caballo_valor_apuesta2()
            resultado_apuesta = pide_datos("Introduce el valor de la apuesta del caballo")
            recoger_Datos_caballos = recoger_datos_caballos1[0]
            valor_apuesta1 = recoger_Datos_caballos.valor_apuesta
            recoger_Datos_caballos2 = recoger_datos_caballos1[1]
            valor_apuesta2 = recoger_Datos_caballos2.valor_apuesta
            recoger_datos = recoger_datos_gran_premio1[1]

            numero_carreras = int(recoger_datos.num_carreras)
            while numero_vueltas < numero_carreras:
                resultado_caballo1 = caballo.avanzar_caballos()
                resultado_caballo2 = caballo.avanzar_caballos2()
                numero_vueltas += 1


        elif opcion == 3:
            print("Adios")
            salir = True
        else:
            pide_datos("Introduce la opcion correcta")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
