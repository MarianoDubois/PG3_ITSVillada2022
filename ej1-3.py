from funciones3 import *

forma = int(input("introduzca la forma que desea hacer 1.Rectangulo 2.Triangulo 3.Todos: "))

if forma == 1:
    alto = int(input("introduzca el alto de su rectangulo: "))
    ancho = int(input("introduzca el ancho de su rectangulo: "))
    relleno = input("introduzca el caracter con el que desea rellenar su rectangulo: ")
    rectangulo(alto, ancho, relleno)
elif forma == 2:
    dimensiones = int(input("introduzca de cunato x cuanto va a ser su triangulo: "))
    relleno = input("introduzca el caracter con el que desea rellenar su triangulo: ")
    triangulo(dimensiones, relleno)
elif forma == 3:
    alto = int(input("introduzca el alto de su rectangulo: "))
    ancho = int(input("introduzca el ancho de su rectangulo: "))
    dimensiones = int(input("introduzca de cunato x cuanto va a ser su triangulo: "))    
    relleno = input("introduzca el caracter con el que desea rellenar su rectangulo: ")
    rectangulo(alto, ancho, relleno)
    triangulo(dimensiones, relleno)   