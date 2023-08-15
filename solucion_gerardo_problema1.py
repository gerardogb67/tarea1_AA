ejemplo1 = [[True, False, True], 
           [False, True, False],
           [False, False, True]]

ejemplo2 = [[True, False, True], # No tiene solucion 
            [False, False, False],
            [True, True, True]]

ejemplo3 = [[True, False, True], 
            [False, True, False],
            [True, True, False],
            [False, False, True],
            [True, True, True]]
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
    a = False
    b = False
    c = False

    flag = False # Bandera que indica si ya se encontro una solucion para el conjunto de clausulas. 1
    cant_clausulas = len(conjunto) # 1
    for i in range (1,8): # Itera un maximo de 7 veces ya que solo hay 8 combinaciones posibles. 1
        for j in range (cant_clausulas): # Segun los valores actuales de a,b,c compara si para todas las clausulas es True. n
            if (not ((conjunto[j][0] and a) or (conjunto[j][1] and b) or (conjunto[j][2] and c))): # Sale del ciclo si una de las clausulas no lo es. 1
                break
            if (j == 2): # Si la iteracion llego a i = 2 hasta este punto quiere decir que se encontro una solucion. 1
                flag = True
                break
        if (flag): break # Si la bandera esta activa quiere decir que se encontró una solución. 1
        a = get_a(i) # 1
        b = get_b(i) # 1
        c = get_c(i) # 1
    if (flag):
        print("Sí (A: ", a,", B: ",b, ", C: ", c,")") 
    else: 
        print ("No :/")

solucion(ejemplo1)
solucion(ejemplo2)
solucion(ejemplo3)

        

