nombre = "Carlos"
edad = 18

if nombre == "Juan": #es juan? si es juan
    if edad >= 18: #tiene mas ded 18? si tiene mas de 18
        print("Eres Juan y tienes mayoria de edad") #entonces ejecutame este mensaje.
    else: #pero si no tiene mas de 18, ejecuta este mensaje.
        print("Eres Juan, pero no tienes mayoria de edad")
else:
    print("Tu no eres Juan")


#El programa primero ve las variables y asigna sus valores.
#Luego llega la primer condicional, nombre es = juan, entonces ejecuta la parte del if del codigo.
#Al haber otro if dentro, ahora verifica si edad= 18, entonces ejecuta "eres juan y tienes mayoria de edad"
#Si el nombre no es Juan, solo se queda en el primer if, es juan? no, no es juan. Entonces ejecuta el else "Tu no eres Juan"
#Una condicion que evalue todos los datos que ya tengo.
