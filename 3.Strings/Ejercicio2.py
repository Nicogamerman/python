#Crear un programa que tenga una variable con la cadena "Separado" y un caracter de coma (,); e inserte el caracter entre cada letra de la cadena. ej: separar y , deberia devolver s,e,p,a,r,a,r
#Pista: Debes utilizar el metodo de las cadenas llamado "Replace" recuerda que la psocion de los caracteres empieza en 0.

palabra= "Separado"

cadena = "Este es el uso del metodo Replace"

reemplazar = cadena.replace("e" , "E") #voy a llamar a la cadena y coloco un replace, luego coloco lo que va a ser reemplazdo por lo que quiero que sea actualmente. 
print(reemplazar) #Ahora todas las e son E
print(palabra)
reemplazar = palabra.replace("", ",")
print(reemplazar)