cadena = "Te quiero solo como amigo"
print (cadena[0:2])
print(cadena[22:25]) #no es lo mas eficiente
print(cadena[-3: ]) #asi es mas eficiente
print(cadena[ : : 2]) #asi imprimo cada dos caracteres, el programa lee T ueosl etc..
print(cadena [ : : -1]) #empieza la cuenta desde atras e imprimi todo.
print(cadena + cadena[ : : -1]) #va a realizar una cadena, mas otra cadena a la inversa.