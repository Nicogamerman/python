letra = "o"

if letra.lower() == "a": #usamos el .lower para indicar que la convierta a minuscula, Si no lo usamos tira error.
    print("Esta vocal es la A")
elif letra.lower()== "e":#sirve para poner mas condiciones que si fuese un else simplemente. Este elif va ligado al if anterior.
    print("Esta vocal es la E")
elif letra.lower()== "i":
    print("Esta vocal es la I")
elif letra.lower()== "o":
    print("Esta letra es la O")
else:#puedo usar else al final, ya que si ninguna de las otras condiciones se cumple, solo queda la posibilidada de que sea U
    print("Esta vocal es la U")

#Python primero toma la letra y revisa, letra.lower es == a? , no eso es falso. Entonces no ejecuta esta parte del codigo.
#Luego revisa elif y pregunta si letra.lower es = e, entonces el programa ejecuta esta parte.