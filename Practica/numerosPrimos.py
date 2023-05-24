#Crear una funcion que nos devuelva los numeros primos entre 0 y el argumento que le pasamos 

#crear funcion que verifique si es primo
def obtenerNumerosPrimos(limite):
    numerosPrimos = []
    #verificamos que el numero pasado no pueda dividirse por ningun numero entre 2 y ese mismo numero -1
    for i in range(2,limite-1):
        #si es divisible poir alguno retornamos false y termina el bucle
        if limite%i == 0: return False
        #si termina el bucle, significa que no fue divisible entonces es primo
    return True

#creamos una funcion que retorne una lista con todos los primos
def primoHasta(limite):
    #creamos la lista
    numerosPrimos = []
    #verificamos si el valor es primo
    for i in range (3,limite+1):
        resultado= obtenerNumerosPrimos(i)
        #si es primo lo devolvemos a la lista
        if resultado == True: numerosPrimos.append(i)
        #devolvemos la lista
    return numerosPrimos
#creamos el resultado llamando a la funcion y lo mostramos
resultado = primoHasta(40)
print(resultado)



