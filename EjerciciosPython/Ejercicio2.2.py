# Ejercicio 2.2 Python

print("Introduce tres valores numéricos \n")

num1 = int(input())
num2 = int(input())
num3 = int(input())

def max(num1, num2, num3):
    if num1 > num2 and num1 > num3 :
        print(num1, "es mayor que", num2, "y", num3)
    elif (num2 > num1) and num2 > num3 :
        print(num2, "es mayor que", num1, "y", num3)
    elif (num3 > num1) and num3 > num2 :
        print(num3, "es mayor que", num1, "y", num2)
    else:
        print ("No se cumplen las condiciones indicadas en el ejercicio \n")

max(num1, num2, num3)