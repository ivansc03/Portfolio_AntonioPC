# Ejercicio 2.1 Python

print("Introduce dos valores numéricos \n")

num1 = int(input())
num2 = int(input())

def max(num1,num2):
    if(num1 > num2) :
        print(num1, "es mayor que", num2)
    else:
        print(num2, "es mayor que", num1)

max(num1,num2)