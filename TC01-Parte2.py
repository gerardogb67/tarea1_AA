
matrizEvaluar = [[1,5,9],[10,11,13],[12,13,15]]
k = 9

def find_value():
    global matrizEvaluar
    global k

    cantColumns = len(matrizEvaluar[0])
    closer = k

    for i in range(len(matrizEvaluar)):
        near = (i + 1) * cantColumns

        if  abs(k - near) < abs(k - closer * cantColumns):
            closer = i
    
    near = cantColumns
    cantRows = abs((closer * 3) - (k - 1))
    print(matrizEvaluar[closer][cantRows])

find_value()
