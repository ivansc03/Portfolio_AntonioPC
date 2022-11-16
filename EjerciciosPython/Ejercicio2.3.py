#Ejercicio 2.3 Python

print("Introduce una palabra \n")

palabra = input()

def caracteres(palabra):
    contador = 0
    for i in palabra:
        contador+=1
    print(contador)

caracteres(palabra)