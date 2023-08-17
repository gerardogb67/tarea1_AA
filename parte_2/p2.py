lista = [0,1,2,3,4,5,6,7,8,9,10]

def binary_search(arr, target):
    min = 0
    max = len(lista) -1
    while (min <= max):
        mid = (min + max) // 2
        if target == lista[mid]:
            return mid
        elif target < lista[mid]:
            max = mid -1
        else:
            min = mid + 1
    return -1

def solucion(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
print(solucion(lista, 9))
    