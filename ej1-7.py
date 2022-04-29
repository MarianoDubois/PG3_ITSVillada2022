numeroString = input("introduzca un numero: ")


def step(numeroString):
    numeroLista=list(numeroString)
    for i in range(len(numeroString)):
        if int(numeroLista[i]) == int(numeroLista[i + 1]) + 1 or int(numeroLista[i]) == int(numeroLista[i + 1]) - 1:
            return "es step"
        else:
            return "no es step"

print(step(numeroString))