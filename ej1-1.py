lista = [8,12,9,45]
objetivo = int(input("introduzca el numero que busca:"))

def busqueda(objetivo, lista):
    index = lista.index(objetivo)
    print(f'The index of {objetivo} is:', index)

busqueda(objetivo, lista)