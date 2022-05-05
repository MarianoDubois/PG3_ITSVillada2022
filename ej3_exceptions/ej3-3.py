while True:
    try:
        meses = ("enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre")
        numeroMes = int(input("pone el numero de mes que quieras: "))
        print(meses[numeroMes-1])
    except IndexError:
        print("taria bueno que pongas un mes que exista no?")
