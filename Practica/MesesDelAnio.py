# Definir la tupla con los meses del año
meses_del_anio = ("enero", "febrero", "marzo", "abril", "mayo", "junio",
"julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre")

# Solicitar al usuario que ingrese un número de mes
numero_mes = int(input("Ingresa un número de mes: "))

# Verificar si el número de mes ingresado es válido
while numero_mes < 1 or numero_mes > 12:
    print("Número de mes inválido. Debe estar entre 1 y 12.")
    numero_mes = int(input("Ingresa otro número de mes (1-12): "))

# Obtener el mes correspondiente de la tupla
mes_elegido = meses_del_anio[numero_mes - 1]

# Mostrar el mes seleccionado
print("El mes seleccionado es:", mes_elegido)
