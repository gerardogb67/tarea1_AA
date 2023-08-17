matriz = [[1,5,9],
          [10,11,13],
          [12,13,15]] 

def solution(matriz, k):
    matriz_unificada = []
    for arreglo in matriz:
        for elemento in arreglo:
            matriz_unificada.append(elemento)
    matriz_unificada.sort()
    return matriz_unificada[k-1]

print(solution(matriz, 9))