import random


probabilities = [0.3, 0.4, 0.3]

price_papers = 1.5
sale_price = 2.5
refund = 0.5



#Simulacion :
iterations = [30,360, (360*10)]

for i in range(len(iterations)):
    #revenue al vender
    revenue9 = 0
    revenue10 = 0
    revenue11 = 0
    for j in range(iterations[i]):
        u= random.random()
        #(Vendi - gaste) + reembolso
        #sale price * pidieron - price_papers * compre
        if u <= probabilities[0]:
            #me pidieron 9

            #Compre 9
            revenue9 += (sale_price*9 - price_papers*9)
            #Compre 10
            revenue10 += (sale_price*9 - price_papers*10)+refund
            #Compre 11
            revenue11 += (sale_price*9 - price_papers*11)+refund*2

        elif u <= (probabilities[1]+probabilities[0]) and u>probabilities[0]:
            #me pidieron 10

            #Compre 9
            revenue9 += (sale_price*9 - price_papers*9) #PREGUNTAR, SI ME HACE FALTA, y si esta bien lo de cambiar los sale price porque no pude vendder esos si no los tengo
            #Compre 10
            revenue10 += (sale_price*10 - price_papers*10)
            #Compre 11
            revenue11 += (sale_price*10 - price_papers*11)+refund
        elif u <= (probabilities[2]+probabilities[1]+probabilities[0]) and u>(probabilities[1]+probabilities[0]):
            #me pidieron 11

            #Compre 9
            revenue9 += (sale_price*9 - price_papers*9)
            #Compre 10
            revenue10 += (sale_price*10 - price_papers*10)
            #Compre 11
            revenue11 += (sale_price*11 - price_papers*11)

    print(f"Ganancia total simulando para {iterations[i]} dias\n")
    print(revenue9)
    print(revenue10)
    print(revenue11)


