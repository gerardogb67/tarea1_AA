import timeit
import matplotlib.pyplot as plt

conjunto_1 = [[True, True, True]] # (A v B v C)

conjunto_2 = [[True, True, False], # (A ∨ B ∨ ¬C) ∧ (A ∨ ¬B ∨ ¬C)
              [True, False, False]]

conjunto_3 = [[True, False, True], # (A ∨ ¬B ∨ C) ∧ (¬A ∨ B ∨ ¬C) ∧ (¬A ∨ ¬B ∨ C)
              [False, True, False],
              [False, False, True]]

conjunto_4 = [[True, False, True], # (A ∨ ¬B ∨ C) ∧ (A ∨ B ∨ C) ∧ (¬A ∨ B ∨ C) ∧ (¬A ∨ ¬B ∨ ¬C)
              [True, True, True],
              [False, True, True],
              [False, False, False]]

conjunto_5 = [[False, False, False], # (¬A ∨ ¬B ∨ ¬C) ∧ (¬A ∨ ¬B ∨ C) ∧ (¬A ∨ B ∨ ¬C) ∧ (A ∨ B ∨ ¬C) ∧ (A ∨ B ∨ ¬C)
              [False, False, True],
              [False, True, False],
              [True, True, False],
              [True, True, False]]

conjunto_6 = [[False, True, False], # (¬A ∨ B ∨ ¬C) ∧ (A ∨ B ∨ C) ∧ (¬A ∨ B ∨ C) ∧ (A ∨ B ∨ ¬C) ∧ (A ∨ ¬B ∨ C) ∧ (A ∨ ¬B ∨ ¬C)
              [True, True, True],
              [False, True, True],
              [True, True, False],
              [True, False, True],
              [True, False, False]]

conjunto_7 = [[False, False, False], # (¬A ∨ ¬B ∨ ¬C) ∧ (¬A ∨ B ∨ C) ∧ (¬A ∨ ¬B ∨ C) ∧ (A ∨ B ∨ ¬C) ∧ (A ∨ ¬B ∨ C) ∧ (A ∨ B ∨ C) ∧ (¬A ∨ B ∨ ¬C)
              [False, True, True],
              [False, False, True],
              [True, True, False],
              [True, False, True],
              [True, True, True],
              [False, True, False]]

conjunto_8 = [[False, True, True], # (¬A ∨ B ∨ C) ∧ (A ∨ B ∨ ¬C) ∧ (A ∨ ¬B ∨ C) ∧ (A ∨ ¬B ∨ ¬C) ∧ (¬A ∨ ¬B ∨ C) ∧ (¬A ∨ B ∨ ¬C) ∧ (A ∨ B ∨ ¬C) ∧ (A ∨ B ∨ C)
              [True, True, False],
              [True, False, True],
              [True, False, False],
              [False, False, True],
              [False, True, True],
              [True, True, False],
              [True, True, True]]

conjunto_9 = [[False, False, False], # (¬A ∨ ¬B ∨ ¬C) ∧ (¬A ∨ ¬B ∨ ¬C) ∧ (¬A ∨ ¬B ∨ ¬C) ∧ (¬A ∨ ¬B ∨ ¬C) ∧ (A ∨ B ∨ C) ∧ (A ∨ ¬B ∨ ¬C) ∧ (A ∨ B ∨ C) ∧ (A ∨ B ∨ ¬C) ∧ (A ∨ B ∨ ¬C)
              [False, False, False],
              [False, False, False],
              [False, False, False],
              [True, True, True],
              [True, False, False],
              [True, True, True],
              [True, True, False],
              [True, True, False]]

conjunto_10 = [[False, False, False], # (¬A ∨ ¬B ∨ ¬C) ∧ (A ∨ B ∨ ¬C) ∧ (A ∨ B ∨ ¬C) ∧ (A ∨ ¬B ∨ C) ∧ (¬A ∨ B ∨ ¬C) ∧ (¬A ∨ ¬B ∨ C) ∧ (¬A ∨ B ∨ C) ∧ (A ∨ ¬B ∨ C) ∧ (A ∨ B ∨ ¬C) ∧ (¬A ∨ B ∨ ¬C)
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

listIteraciones = []
listTimes = []
listResultados = []
# Segun el numero de la iteracion, se obtienen los valores de los booleanos que se estan usando para buscar soluciones
def get_a(numero):
    value_post_shr = numero >> 2
    return value_post_shr & 1
def get_b(numero):
    value_post_shr = numero >> 1
    return value_post_shr & 1
def get_c(numero):
    return numero & 1
def get_value_of_variable(variable_1, variable_2):
    if (not variable_1): 
        return not variable_2
    return variable_2
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
            if (not (get_value_of_variable(conjunto[j][0], a) or get_value_of_variable(conjunto[j][1], b) or get_value_of_variable(conjunto[j][2], c))): # Sale del ciclo si una de las clausulas no lo es. 1
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
    listResultados.append(False)
else: 
    print("     Sí (A:", solucion_1[0], ", B:", solucion_1[1], ", C:", solucion_1[2], ")")
    listResultados.append(True)
listIteraciones.append(contador_iteraciones)
contador_iteraciones = 0

print("Conjunto 2: ") 
solucion_2 = solucion(conjunto_2) 
if solucion_2 == []:
    print("     No tiene solucion")
    listResultados.append(False)
else: 
    print("     Sí (A:", solucion_2[0], ", B:", solucion_2[1], ", C:", solucion_2[2], ")")
    listResultados.append(True)
listIteraciones.append(contador_iteraciones)
contador_iteraciones = 0

print("Conjunto 3: ") 
solucion_3 = solucion(conjunto_3) 
if solucion_3 == []:
    print("     No tiene solucion")
    listResultados.append(False)
else: 
    print("     Sí (A:", solucion_3[0], ", B:", solucion_3[1], ", C:", solucion_3[2], ")")
    listResultados.append(True)
listIteraciones.append(contador_iteraciones)
contador_iteraciones = 0

print("Conjunto 4: ") 
solucion_4 = solucion(conjunto_4) 
if solucion_4 == []:
    print("     No tiene solucion")
    listResultados.append(False)
else: 
    print("     Sí (A:", solucion_4[0], ", B:", solucion_4[1], ", C:", solucion_4[2], ")")
    listResultados.append(True)
listIteraciones.append(contador_iteraciones)
contador_iteraciones = 0

print("Conjunto 5: ") 
solucion_5 = solucion(conjunto_5) 
if solucion_5 == []:
    print("     No tiene solucion")
    listResultados.append(False)
else: 
    print("     Sí (A:", solucion_5[0], ", B:", solucion_5[1], ", C:", solucion_5[2], ")")
    listResultados.append(True)
listIteraciones.append(contador_iteraciones)
contador_iteraciones = 0

print("Conjunto 6: ") 
solucion_6 = solucion(conjunto_6) 
if solucion_6 == []:
    print("     No tiene solucion")
    listResultados.append(False)
else: 
    print("     Sí (A:", solucion_6[0], ", B:", solucion_6[1], ", C:", solucion_6[2], ")")
    listResultados.append(True)
listIteraciones.append(contador_iteraciones)
contador_iteraciones = 0

print("Conjunto 7: ") 
solucion_7 = solucion(conjunto_7) 
if solucion_7 == []:
    print("     No tiene solucion")
    listResultados.append(False)
else: 
    print("     Sí (A:", solucion_7[0], ", B:", solucion_7[1], ", C:", solucion_7[2], ")")
    listResultados.append(True)
listIteraciones.append(contador_iteraciones)
contador_iteraciones = 0

print("Conjunto 8: ") 
solucion_8 = solucion(conjunto_8) 
if solucion_8 == []:
    print("     No tiene solucion")
    listResultados.append(False)
else: 
    print("     Sí (A:", solucion_8[0], ", B:", solucion_8[1], ", C:", solucion_8[2], ")")
    listResultados.append(True)
listIteraciones.append(contador_iteraciones)
contador_iteraciones = 0

print("Conjunto 9: ") 
solucion_9 = solucion(conjunto_9) 
if solucion_9 == []:
    print("     No tiene solucion")
    listResultados.append(False)
else: 
    print("     Sí (A:", solucion_9[0], ", B:", solucion_9[1], ", C:", solucion_9[2], ")")
    listResultados.append(True)
listIteraciones.append(contador_iteraciones)
contador_iteraciones = 0

print("Conjunto 10: ") 
solucion_10 = solucion(conjunto_10) 
if solucion_10 == []:
    print("     No tiene solucion")
    listResultados.append(False)
else: 
    print("     Sí (A:", solucion_10[0], ", B:", solucion_10[1], ", C:", solucion_10[2], ")")
    listResultados.append(True)
listIteraciones.append(contador_iteraciones)
contador_iteraciones = 0

for i in range(1, 11):
    code_to_measure = "solucion(conjunto_"+str(i)+")"
    execution_time = timeit.timeit(stmt = code_to_measure, setup = "from __main__ import solucion, conjunto_"+str(i), number = 1)
    listTimes.append(execution_time)
    # if (flag):
    #     print("Sí (A: ", a,", B: ",b, ", C: ", c,")") 
    # else: 
    #     print ("No :/")

def table_data():
    global listIteraciones
    global listTimes
    global listResultados

    # Se agrupan los datos a mostrar con su correspondiente de cada lista
    cantidadClausulas = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    datosMostrar = list(zip(cantidadClausulas, listResultados, listIteraciones, listTimes))

    # Crea la ventana donde se va a mostrar la tabla y le pone un limitante 
    # (márgenes) para que la misma se muestre 
    fig, ax = plt.subplots(figsize=(8, 5))
    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)

    # Se crea la tabla con los encabezados y datos a mostrar
    tabla = ax.table(cellText=datosMostrar,
        colLabels=["Cant. Clausulas", "Resultado", "Interaciones", "Tiempo"],
        cellLoc="center", loc="center")

    # Personalización de la table
    tabla.auto_set_font_size(False)
    tabla.set_fontsize(8)
    tabla.scale(1.2, 1.2)
    plt.title('Tabla Resumen con los Datos Recolectados en la Prueba')
    ax.axis("off")

    # Muestra la ventana con la tabla en pantalla
    plt.show()
table_data()

def graphic_time():
    global listTimes

    # Datos a mostrar en el gráfico (x = Cantidad de cláusulas, y = iteraciones)
    x = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    y = listTimes

    plt.figure(figsize=(8, 6))
    plt.subplots_adjust(left=0.15, right=0.95, top=0.9, bottom=0.1)

    # Crear el gráfico
    plt.plot(x, y, label='Duración', color="blue", linewidth = 3)
    plt.scatter(x, y, color='cyan', label='Valores',linewidths = 4)
    
    # Agregar etiquetas y título
    plt.xlabel('Cantidad de cláusulas')
    plt.ylabel('Tiempo de ejecución')
    plt.title('Gráfico del Tiempo de Ejecución en los Conjuntos Prueba')

    # Agregar leyenda
    plt.legend()

    # Mostrar el gráfico
    plt.show()
graphic_time()