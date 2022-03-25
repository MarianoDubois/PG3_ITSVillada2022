año = int(input("que año desea saber si es biciesto?"))

def biciesto(año):
    if año%4 == 0:
        if año%100 == 0:
            if año%400 == 0:
                print(f"{año} es biciesto")
            else:
                print(f"{año} no es biciesto")
        else:
            print(f"{año} es biciesto")
    else:
        print(f"{año} no es biciesto")


biciesto(año)