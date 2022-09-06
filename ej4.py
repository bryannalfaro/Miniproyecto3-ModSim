#Universidad del Valle de Guatemala
#Modelacion y simulacion
#Ejercicio 4 - Miniproyecto 3
#Autores:
#   - 19372 Bryann Alfaro
#   - 19422 Diego Arredondo
import random
import re


#Settear valores de costos
probabilities = [0.3, 0.4, 0.3]
price_papers = 1.5
sale_price = 2.5
refund = 0.5



#Simulacion :
iterations = [30,360, (360*10)]

#Se recorre el array de iterations
for i in range(len(iterations)):
    #Se inicializan las variables para almacenar ganancias
    revenue9 = 0
    revenue10 = 0
    revenue11 = 0

    #Se inicializan las variables para las perdidas
    loss9 = 0
    loss10 = 0
    loss11 = 0
    #Se recorre la cantidad de veces (30,360,3600)
    for j in range(iterations[i]):
        u= random.random() # Se genera valor aleatorio


        #Formula a utilizar para calculo de ganancia
        #(Vendi - gaste) + reembolso

        #Se utiliza transformacion inversa para la evaluacion de la probabilidad
        if u <= probabilities[0]:
            #Se evalua si me pidieron 9 periodicos

            #Compre 9 periodicos
            revenue9 += (sale_price*9 - price_papers*9)
            #Compre 10 periodicos
            revenue10 += (sale_price*9 - price_papers*10)+refund
            #Compre 11 periodicos
            revenue11 += (sale_price*9 - price_papers*11)+refund*2

        elif u <= (probabilities[1]+probabilities[0]) and u>probabilities[0]:
            #Se evalua si me pidieron 10 periodicos

            #Compre 9 periodicos
            revenue9 += (sale_price*9 - price_papers*9)
            loss9 +=1
            #Compre 10 periodicos
            revenue10 += (sale_price*10 - price_papers*10)
            #Compre 11 periodicos
            revenue11 += (sale_price*10 - price_papers*11)+refund
        elif u <= (probabilities[2]+probabilities[1]+probabilities[0]) and u>(probabilities[1]+probabilities[0]):
            #Se evalua si me pidieron 11 periodicos

            #Compre 9 periodicos
            revenue9 += (sale_price*9 - price_papers*9)
            loss9 +=2
            #Compre 10 periodicos
            revenue10 += (sale_price*10 - price_papers*10)
            loss10 +=1
            #Compre 11 periodicos
            revenue11 += (sale_price*11 - price_papers*11)

    #Se imprime el resultado de la simulacion
    print("*"*50)
    print(f"Ganancia total simulando para {iterations[i]} dias\n")
    print(revenue9 ,'para 9 periodicos')
    print(revenue10,'para 10 periodicos')
    print(revenue11,'para 11 periodicos')

    print(f"Perdida total simulando para {iterations[i]} dias\n")
    print(loss9,'para 9 periodicos')
    print(loss10,'para 10 periodicos')
    print(loss11,'para 11 periodicos')
    print("*"*50)

    #Se evalua la mejor cantidad de periodicos a comprar
    revenues ={9:revenue9, 10:revenue10, 11:revenue11}
    #Se ordena de mayor a menor el diccionario
    revenues = sorted(revenues.items(), key=lambda x: x[1], reverse=True)
    losses = {'9':loss9, '10':loss10, '11':loss11}

    #Se obtienen los 2 primeros valores mayores y se les resta su perdida
    first = revenues[0][1] - losses.get(str(revenues[0][0]))
    second = revenues[1][1] - losses.get(str(revenues[1][0]))

    #Se evalua si el primer elemento sigue siendo el de mayor ganancia o no
    if first>second:
        print(f"Comprar {revenues[0][0]}")
    else:
        print(f"Comprar {revenues[1][0]}")


