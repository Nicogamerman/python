lista = ["Python" , 24 , "Rene" , "alexander" , 12]

lista[3] = "Alexander"
print(lista)

lista.pop() #Elimina el ultimo dato de la lista
print(lista)
lista.pop() #Ahora me elimina el anteultimo
print(lista)

lista.remove("Python") #elimina el valor que yo quiero
print(lista)