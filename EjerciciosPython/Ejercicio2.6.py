#Ejercicio 2.6 Python

print("Introduce una cadena de caracteres \n")

cadena = input()

def inversa(cadena):
    if len(cadena) == 0:
        return cadena
    else:
        return inversa(cadena[1:]) + cadena[0]
print ("La cadena original es:", cadena)
print ("La cadena invertida es:", inversa(cadena))