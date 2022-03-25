lista = [3, 5, 1, 6, 0, 2, 7, 8]

def ordenar(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1] :
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    print(arr)

ordenar(lista)