import timeit

conjunto_1 = [[True, True, True]] # (A v B v C)

conjunto_2 = [[True, True, False],
              [True, False, False]]

conjunto_3 = [[True, False, True],
              [False, True, False],
              [False, False, True]]

conjunto_4 = [[True, False, True],
              [True, True, True],
              [False, True, True],
              [False, False, False]]

conjunto_5 = [[False, False, False],
              [False, False, True],
              [False, True, False],
              [True, True, False],
              [True, True, False]]

conjunto_6 = [[False, True, False],
              [True, True, True],
              [False, True, True],
              [True, True, False],
              [True, False, True],
              [True, False, False]]

conjunto_7 = [[False, False, False],
              [False, True, True],
              [False, False, True],
              [True, True, False],
              [True, False, True],
              [True, True, True],
              [False, True, False]]

conjunto_8 = [[False, True, True],
              [True, True, False],
              [True, False, True],
              [True, False, False],
              [False, False, True],
              [False, True, True],
              [True, True, False],
              [True, True, True]]

conjunto_9 = [[False, False, False],
              [False, False, False],
              [False, False, False],
              [False, False, False],
              [True, True, True],
              [True, False, False],
              [True, True, True],
              [True, True, False],
              [True, True, False]]

conjunto_10 = [[False, False, False],
               [True, True, False],
               [True, True, False],
               [True, False, True],
               [False, True, False],
               [False, False, True],
               [False, True, True],
               [True, False, True],
               [True, True, False],
               [False, True, False]]

contador_iteraciones = 0
# Segun el numero de la iteracion, se obtienen los valores de los booleanos que se estan usando para buscar soluciones
def get_a(numero):
    value_post_shr = numero >> 2
    return value_post_shr & 1
def get_b(numero):
    value_post_shr = numero >> 1
    return value_post_shr & 1
def get_c(numero):
    return numero & 1

def solucion(conjunto): # n
    global contador_iteraciones
    a = False
    b = False
    c = False

    flag = False # Bandera que indica si ya se encontro una solucion para el conjunto de clausulas. 1
    cant_clausulas = len(conjunto) # 1
    for i in range (1,8): # Itera un maximo de 7 veces ya que solo hay 8 combinaciones posibles. 1
        contador_iteraciones += 1
        for j in range (cant_clausulas): # Segun los valores actuales de a,b,c compara si para todas las clausulas es True. n
            contador_iteraciones += 1
            if (not ((conjunto[j][0] and a) or (conjunto[j][1] and b) or (conjunto[j][2] and c))): # Sale del ciclo si una de las clausulas no lo es. 1
                break
            if (j == cant_clausulas-1): # Si la iteracion llego a i = 2 hasta este punto quiere decir que se encontro una solucion. 1
                flag = True
                break
        if (flag): break # Si la bandera esta activa quiere decir que se encontró una solución. 1
        a = get_a(i) # 1
        b = get_b(i) # 1
        c = get_c(i) # 1
    if (flag):
        return [a,b,c]
    else: 
        return []

solucion_1 = solucion(conjunto_1)
print("Conjunto 1: ") 
if solucion_1 == []:
    print("     No tiene solucion")
else: 
    print("     Sí (A:", solucion_1[0], ", B:", solucion_1[1], ", C:", solucion_1[2], ")")
print("Iteraciones: " + str(contador_iteraciones))
contador_iteraciones = 0

print("Conjunto 2: ") 
solucion_2 = solucion(conjunto_2) 
if solucion_2 == []:
    print("     No tiene solucion")
else: 
    print("     Sí (A:", solucion_2[0], ", B:", solucion_2[1], ", C:", solucion_2[2], ")")
print("Iteraciones: " + str(contador_iteraciones))
contador_iteraciones = 0

print("Conjunto 3: ") 
solucion_3 = solucion(conjunto_3) 
if solucion_3 == []:
    print("     No tiene solucion")
else: 
    print("     Sí (A:", solucion_3[0], ", B:", solucion_3[1], ", C:", solucion_3[2], ")")
print("Iteraciones: " + str(contador_iteraciones))
contador_iteraciones = 0

print("Conjunto 4: ") 
solucion_4 = solucion(conjunto_4) 
if solucion_4 == []:
    print("     No tiene solucion")
else: 
    print("     Sí (A:", solucion_4[0], ", B:", solucion_4[1], ", C:", solucion_4[2], ")")
print("Iteraciones: " + str(contador_iteraciones))
contador_iteraciones = 0

print("Conjunto 5: ") 
solucion_5 = solucion(conjunto_5) 
if solucion_5 == []:
    print("     No tiene solucion")
else: 
    print("     Sí (A:", solucion_5[0], ", B:", solucion_5[1], ", C:", solucion_5[2], ")")
print("Iteraciones: " + str(contador_iteraciones))
contador_iteraciones = 0

print("Conjunto 6: ") 
solucion_6 = solucion(conjunto_6) 
if solucion_6 == []:
    print("     No tiene solucion")
else: 
    print("     Sí (A:", solucion_6[0], ", B:", solucion_6[1], ", C:", solucion_6[2], ")")
print("Iteraciones: " + str(contador_iteraciones))
contador_iteraciones = 0

print("Conjunto 7: ") 
solucion_7 = solucion(conjunto_7) 
if solucion_7 == []:
    print("     No tiene solucion")
else: 
    print("     Sí (A:", solucion_7[0], ", B:", solucion_7[1], ", C:", solucion_7[2], ")")
print("Iteraciones: " + str(contador_iteraciones))
contador_iteraciones = 0

print("Conjunto 8: ") 
solucion_8 = solucion(conjunto_8) 
if solucion_8 == []:
    print("     No tiene solucion")
else: 
    print("     Sí (A:", solucion_8[0], ", B:", solucion_8[1], ", C:", solucion_8[2], ")")
print("Iteraciones: " + str(contador_iteraciones))
contador_iteraciones = 0

print("Conjunto 9: ") 
solucion_9 = solucion(conjunto_9) 
if solucion_9 == []:
    print("     No tiene solucion")
else: 
    print("     Sí (A:", solucion_9[0], ", B:", solucion_9[1], ", C:", solucion_9[2], ")")
print("Iteraciones: " + str(contador_iteraciones))
contador_iteraciones = 0

print("Conjunto 10: ") 
solucion_10 = solucion(conjunto_10) 
if solucion_10 == []:
    print("     No tiene solucion")
else: 
    print("     Sí (A:", solucion_10[0], ", B:", solucion_10[1], ", C:", solucion_10[2], ")")
print("Iteraciones: " + str(contador_iteraciones))
contador_iteraciones = 0

for i in range(1, 11):
    code_to_measure = "solucion(conjunto_"+str(i)+")"
    execution_time = timeit.timeit(stmt = code_to_measure, setup = "from __main__ import solucion, conjunto_"+str(i), number = 1)
    print(execution_time)
    # if (flag):
    #     print("Sí (A: ", a,", B: ",b, ", C: ", c,")") 
    # else: 
    #     print ("No :/")