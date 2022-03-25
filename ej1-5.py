ans = input("ponga una palabra: ")

def capicua(str):
    for i in range(0, int(len(str)/2)):
        if str[i] != str[len(str)-i-1]:
            return print(f"{str} no es capicua")
    return print(f"{str} es capicua")

capicua(ans)