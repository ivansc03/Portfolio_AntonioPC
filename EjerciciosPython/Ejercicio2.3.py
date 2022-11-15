#Ejercicio 2.3 Python

# No me muestra cuántos caracteres tiene la palabra

print("Introduce una palabra \n")

palabra = input()

def caracteres(palabra):
    contador = 0
    while True:
        try:
            palabra[contador]
            contador+=1
        except:
            print ("Error \n")
    return contador