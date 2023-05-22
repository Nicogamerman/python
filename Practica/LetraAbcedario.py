# Definir la tupla con las letras del alfabeto
alfabeto = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O",
            "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")

# Solicitar al usuario que ingrese un número
numero = int(input("Ingresa un número (1-26): "))

# Verificar si el número ingresado es válido
if numero >= 1 and numero <= 26:
    # Obtener la letra correspondiente de la tupla
    letra = alfabeto[numero - 1]

    # Mostrar la letra seleccionada
    print("La letra correspondiente es:", letra)
else:
    print("Número inválido. Debe estar entre 1 y 26.")
