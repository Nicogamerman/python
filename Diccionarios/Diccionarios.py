diccionario = {"Nombre" : "Walter" , "Apellido" : "Coto" , "Estatura" : 1.8}

print(diccionario)
print(type(diccionario))

print(diccionario.keys()) #muetra solo las llaves 
print(diccionario.values()) #muestra solo los valores

print(diccionario["Estatura"])

diccionario["Peso"] = "58 kg" #asi podemos agregar un nuevo valor al diccionario
print(diccionario)

diccionario["Nombre"] = "Nicolas" #cambio el valor de walter, por Nicolas
print(diccionario)