letra = input("Ingrese una letra:")

if letra.lower()  == "a":
    print("Es una vocal")
else:
    if letra.lower()== "e":
        print("Es una vocal")
    else:
        if letra.lower()== "i":
            print("Es una vocal")
        else:
            if letra.lower()== "o":
                print("Es una vocal")
            else:
                if letra.lower()== "u":
                    print("Es una vocal")
                else:
                    print("No es una vocal")

#Una forma simplificada de escribir todo un codigo asi es:}
if letra.lower() in "aeiou":
    print("Es una vocal")
else:
    print("NO es una vocal")