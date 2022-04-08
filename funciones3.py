import math

def rectangulo(alto, ancho, relleno):
    for i in range(alto):
        print(str(relleno*ancho))

def triangulo(alto, relleno):
    k = alto - 1
    for i in range(0, alto):
        for j in range(0, k):
            print(end=" ")
        k = k - 1
        for j in range(0, i+1):
            print(f"{relleno} ", end="")
        print("\r")