#Universidad del Valle de Guatemala
#Modelacion y simulacion
#Ejercicio 3 - Miniproyecto 3
#Autores:
#   - 19372 Bryann Alfaro
#   - 19422 Diego Arredondo
import numpy as np
import numpy_financial as npf
from matplotlib import pyplot as plt

#Funcion donde se encuentran los resultados de las distribuciones (normal, uniforme)
#para el hotel
def sim_hotel():
    lista_npv_hotel = [-800]
    lista_npv_hotel.append(np.random.normal(-800,50))
    lista_npv_hotel.append( np.random.normal(-800,100))
    lista_npv_hotel.append( np.random.normal(-700,150))
    lista_npv_hotel.append( np.random.normal(300,200))
    lista_npv_hotel.append( np.random.normal(400,200))
    lista_npv_hotel.append( np.random.normal(500,200))
    lista_npv_hotel.append( np.random.uniform(200,8440))
    return lista_npv_hotel

#Funcion donde se encuentran los resultados de las distribuciones (normal, uniforme)
#para el centro comercial
def sim_centro():
    lista_npv_centro = [-900]
    lista_npv_centro.append(np.random.normal(-600,50))
    lista_npv_centro.append(np.random.normal(-200,50))
    lista_npv_centro.append(np.random.normal(-600,100))
    lista_npv_centro.append(np.random.normal(250,150))
    lista_npv_centro.append(np.random.normal(350,150))
    lista_npv_centro.append(np.random.normal(400,150))
    lista_npv_centro.append(np.random.uniform(1600,6000))
    return lista_npv_centro

#Inicializacion de variables
valorSimulacion = 1000
resultado_hotel = 0
resultado_centro = 0


#Se realiza la simulacion por la cantidad indicada
for i in range(valorSimulacion):
    #Se llama a la funcion que simula el hotel
    lista_hotel = sim_hotel()
    #Se llama a la funcion que simula el centro comercial
    lista_centro = sim_centro()

    #Se calcula el npv para el hotel y centro comercial al 10%
    r1 = npf.npv(0.1, lista_hotel)
    r2 = npf.npv(0.1, lista_centro)

    #Se almacena el resultado del npv
    resultado_hotel += r1
    resultado_centro += r2

#Se calcula el promedio de los resultados
promedio1 = resultado_hotel/valorSimulacion
promedio2 = resultado_centro/valorSimulacion

#Se imprime el resultado
print(f'Promedio del hotel con {valorSimulacion} ejecuciones: ',promedio1)
print(f'Promedio del centro comercial con {valorSimulacion} ejecuciones: ',promedio2)