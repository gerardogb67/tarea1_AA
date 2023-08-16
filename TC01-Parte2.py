
matrizEvaluar = []
k = 0
n = 0


def request_Matrix_K():
    global matrizEvaluar
    global k
    global n

    matrixRows = []
    n = 0

    bandera = False
    while bandera != True:
        n = int(input("Tamaño de la matriz: "))
        if n < 1 or n > 300:
            print("ERROR: El tamaño de la matriz no se encuentra en los parámetros permitidos.")
        else:
            bandera = True

    i = 0
    j = 0
    while i != n:
        print("\nCOMPLETANDO LA FILA ", i)
        while j != n:
            numCol = int(input("Valor de la columna: "))
            if numCol < -1000000000 or numCol > 1000000000:
                print("ERROR: El valor de la columna no se encuentra dentro de los parámetros establecidos.\n")
                j -=1
            else:
                matrixRows.append(numCol)
            
            j += 1
        
        if matrixRows != sorted(matrixRows):
            print("ERROR: Los valores de la fila de la matriz deben estar ordenados de manera ascendente.")
            i -= 1
        else:
            matrizEvaluar.append(matrixRows[:])
        
        matrixRows.clear()
        i += 1
        j = 0

    bandera = False
    while bandera != True:
        k = int(input("\nK-ésimo elemento a buscar: "))
        if k < 1 or k > n ** 2:
            print("ERROR: El K-ésimo elemento ingresado sobrepasa los elementos de la matriz.")
        else:
            bandera = True
    
def check_Matrix():
    global matrizEvaluar
    global n

    for i in range(n - 1):
        num1 = matrizEvaluar[i][n - 1]
        num2 = matrizEvaluar[i + 1][0]
        if num1 > num2:
            matrizEvaluar[i][n - 1] = num2
            matrizEvaluar[i + 1][0] = num1

def find_value():
    global matrizEvaluar
    global k
    global n

    check_Matrix()
    ordenMatrix = len(matrizEvaluar[0])
    closer = k

    for i in range(len(matrizEvaluar)):
        near = (i + 1) * ordenMatrix

        if  abs(k - near) < abs(k - closer * ordenMatrix):
            closer = i
    
    near = ordenMatrix
    posK = abs((closer * 3) - (k - 1))
    print(matrizEvaluar[closer][posK])


request_Matrix_K()
find_value()