P1= float(input("Ingrese nota Practica uno:"))
print(P1)
P2 = float(input("Ingrese nota Practica dos:"))
print(P2)
P3= float(input("Ingrese nota Practica 3:"))
print(P3)
EP= float(input("Ingrese nota Examen parcial:"))
print(EP)
EF = float(input("Ingrese nota Examen final:"))
print(EF)

Prom = (P1+P2+P3) / (3)

print("El promedio del alumno es: ",(((Prom) + (2*EP) + (3*EF)) / (6)))
