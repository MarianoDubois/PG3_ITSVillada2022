ans = input("introduzca una palabra: ")

def cuentaVocales(str):
    count = 0
    vowel = set("aeiouAEIOU")
    for alphabet in str:
        if alphabet in vowel:
            count = count + 1
      
    print("numero de vocales encontradas:", count)

cuentaVocales(ans)