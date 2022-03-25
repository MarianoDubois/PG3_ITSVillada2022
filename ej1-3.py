alto = int(input("introduzca el alto que desea:"))
ancho = int(input("introduzca el ancho que desea:"))
relleno = input("introduzca el caracter que desea de relleno:")

def rectangulo(alto, ancho, relleno):
    for i in range(alto):
        print(str(relleno*ancho))

rectangulo(alto, ancho, relleno)