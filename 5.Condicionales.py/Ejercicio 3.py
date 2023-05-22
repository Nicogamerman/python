#Escribe un programa que pida dos palabras y diga si riman o no. 
#Si coinciden las tres ultimas letras tiene que decir que ruman. 
#Si coinciden solo las dos ultimas tiene que decir que ruman un poco y si no, que no riman.

#extraño <--> tamaño
#desligo <--> amigo
#riman <--> cuerpo
#sol <--> lol
#lo <--> yo

#tenemos 4 condicionales.

palabra1 = input("Ingresa la primer palabra: ")
palabra2 = input("Ingresa la segunda palabra: ")

if len(palabra1) < 3 or len(palabra2) < 3: #palabra 1 sea menor a 3 caracteres, len es para saber cuantos caracteres tiene una strin    
    print("No riman porque tiene menos de 3 caracteres.")
elif palabra1 [-3 : ] == palabra2 [-3 : ]: #los ultimos 3 caracteres de palabra1 son iguales a los ultimos 3 de palabra2? 
    print("Las palabras riman")
elif palabra1[-2 : ] == palabra2 [-2 : ]:
    print("Las palabras riman un poco")
else:
    print("Las palabras no riman")