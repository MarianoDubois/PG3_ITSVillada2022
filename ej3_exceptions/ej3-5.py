try:    
    valor = input("pone lo que quieras: ")
    file = open('readme.txt', 'w')
    file.write("funciona")
    if valor.isnumeric() == True:
        file.write(int(valor))
    else: 
        file.write(valor)
    file.close()
    file = open('readme.txt', 'r')
    print(file.read())
    file.close()
except TypeError:
    file = open('readme.txt', 'w')
    file.write("funciona aun con un problema")
    file.close()
    file = open('readme.txt', 'r')
    print(file.read())
    file.close()