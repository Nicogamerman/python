#Crear un programa que permita al usuario elegir un candidato po el cual votar. Las posibilidades son: candidato A por el partido rojo, candidato B por el partido verde, candidato C por el partido azul. Segun el candidato elegido (A,B,C) se le debe imprimir el mensaje "Usted ha votado por el partido (color que corresponda al candidato elegido)". Si el usuario ingresa una opcion que no corresponde a ninguno de los candidatos disponibles, indicar "opcion erronea"
#Pista: si la letra ingresada por el usuario es en minuscula, el programa debe convertirla en mayuscula.

#A ROJO
#B VERDE
#C AZUL


opcion = input ("Ingresa la opcion de tu candidato(A,B,C): ")
if opcion.upper() == "A":
    print("Usted escogio el candidato Rojo")
elif opcion.upper() == "B":
    print("Usted escogio al candidato Verde")
elif opcion.upper () == "C":
    print("Usted escogio el candidato Azul")
else:
    print("Opcion erronea")