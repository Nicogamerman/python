numero = int(input("Ingrese un número: "))

print("Tablas de multiplicar de", numero)

i = 1
while i <= 10:
    resultado = numero * i
    print("{} x {} = {}".format(numero, i, resultado))
    i += 1
