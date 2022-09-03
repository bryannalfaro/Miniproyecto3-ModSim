import numpy as np
import numpy_financial as npf
from matplotlib import pyplot as plt


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

valorSimulacion = 1000
resultado_hotel = 0
resultado_centro = 0


lista1 = []
lista2 = []


for i in range(valorSimulacion):
    #Hotel
    lista_hotel = sim_hotel()
    #Centro comercial
    lista_centro = sim_centro()
    r1 = npf.npv(0.1, lista_hotel)
    r2 = npf.npv(0.1, lista_centro)

    lista1.append(r1)
    lista2.append(r2)

    resultado_hotel += r1
    resultado_centro += r2

promedio1 = resultado_hotel/valorSimulacion
promedio2 = resultado_centro/valorSimulacion

print(f'Promedio del hotel con {valorSimulacion} ejecuciones: ',promedio1)
print(f'Promedio del centro comercial con {valorSimulacion} ejecuciones: ',promedio2)