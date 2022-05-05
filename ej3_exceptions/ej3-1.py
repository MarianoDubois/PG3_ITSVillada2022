while True:
    try:
        n1 = int(input("pone un n: "))
        n2 = int(input("pone otro n: "))
        suma = n1+n2
        print(suma)
    except ValueError:
        print("pone un numero")
    