#Ejercicio 2.7 Python

lista1 = ["Paco", "Antonio", "Rogelio"]
lista2 = ["Amancio", "Antonio", "Cristóbal"]

def superposicion(lista1,lista2):
    for nombre1 in lista1:
        for nombre2 in lista2:
            if nombre1 == nombre2:
                return True
    return False

print(superposicion(lista1,lista2))