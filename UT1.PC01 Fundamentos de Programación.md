author: Antonio Peñalver Caro
id: Ejercicio UT1.PC01 PPS
categories: Fundamentos de programación
environments: Web
status: Published

## Ejercicio 1

En primer lugar vamos a comprobar las características principales de los lenguajes de programación a través de los ejercicios prácticos que habéis realizado.
Los ejercicios serán los siguientes:

### Lista 1

* Debéis elegir 1 ejercicio de UT1.PC01 Introducción a la programación - Parte 1
* Debéis elegir 2 ejercicios de UT1.PC01 Introducción a la programación - Parte 2

Antes que nada, voy a mostrar las características de los lenguajes de programación que vamos a comparar más tarde a través de los ejercicios que he realizado:

### Características de Python

* Fácil de aprender
* Lenguaje interpretado
* Tipado dinámico
* Fuertemente tipado
* Multiplataforma
* Orientado a objetos
* Indentado
* Seguro

### Características de PHP

* Fácil de aprender
* Orientado al desarrollo de aplicaciones web
* Conectividad con casi todos los motores de BDD
* Confiable y seguro
* Mucha documentación
* Gran ampliación de módulos
* Orientado a objetos
* Posee manejo de excepciones
* No necesita definir tipos de variables

### Características de Java

* Fácil de aprender
* Orientado a objetos
* Distribuido
* Robusto
* Arquitectura neutral
* Seguro
* Portable
* Lenguaje Interpretado
* Multithreaded
* Tipado dinámico

### Comparación Ejercicios 

Los 3 ejercicios que voy a escoger, van a ser: Ejercicio1.2.py, Ejercicio2.2.py y Ejercicio2.3.py.

Algo a destacar del primer ejercicio, es la manera de declarar las variables. Ya que en Python, las variables se declaran sin usar ningún valor literal. Sin embargo, para poder declarar una variable en PHP, hay que usar el valor literal "$" y en Java, se indica el tipo de variable y el identificador de la misma.

print("Introduce dos valores numéricos")
numero1 = int(input())
numero2 = int(input())
if numero1 > numero2 :
    print(numero1, "es mayor que", numero2)
else:
    print(numero1, "es menor que", numero2)
