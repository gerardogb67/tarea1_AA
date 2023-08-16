import matplotlib.pyplot as plt
import time
import timeit

#Variables Globales
listClausulas = []
listLiterales = []
listLetras = []
abecedario = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

rowMatriz = 0
columMatriz = 0
clausula = ""
startTime = 0

listIteraciones = []
listTimes = []
listaResultados = []
counter = 0

# listaConjuntosP = [
#     "(A ∨ B ∨ ¬C) ∧ (A ∨ ¬B ∨ ¬C) ∧ (A ∨ B ∨ C)",
#     "(A ∨ ¬B ∨ C) ∧ (¬A ∨ B ∨ ¬C) ∧ (¬A ∨ ¬B ∨ C)",
#     "(¬A ∨ ¬B ∨ C) ∧ (A ∨ B ∨ C) ∧ (¬A ∨ B ∨ C)",
#     "(A ∨ B ∨ C) ∧ (A ∨ B ∨ C) ∧ (A ∨ B ∨ C)",
#     "(¬A ∨ ¬B ∨ ¬C) ∧ (¬A ∨ ¬B ∨ C) ∧ (¬A ∨ B ∨ ¬C)", 
#     "(¬A ∨ ¬B ∨ ¬C) ∧ (A ∨ B ∨ ¬C) ∧ (A ∨ B ∨ ¬C)",
#     "(¬A ∨ ¬B ∨ ¬C) ∧ (¬A ∨ ¬B ∨ ¬C) ∧ (¬A ∨ ¬B ∨ C)", 
#     "(A ∨ B ∨ ¬C) ∧ (A ∨ ¬B ∨ C) ∧ (A ∨ ¬B ∨ ¬C)",
#     "(¬A ∨ B ∨ C) ∧ (A ∨ ¬B ∨ C) ∧ (A ∨ B ∨ ¬C)",
#     "(A ∨ ¬B ∨ ¬C) ∧ (¬A ∨ B ∨ C) ∧ (¬A ∨ ¬B ∨ ¬C)" 
# ]

listaConjuntosP = [
    "(A ∨ B ∨ C)",
    "(A ∨ B ∨ ¬C) ∧ (A ∨ ¬B ∨ ¬C)",
    "(A ∨ ¬B ∨ C) ∧ (¬A ∨ B ∨ ¬C) ∧ (¬A ∨ ¬B ∨ C)",
    "(A ∨ ¬B ∨ C) ∧ (A ∨ B ∨ C) ∧ (¬A ∨ B ∨ C) ∧ (¬A ∨ ¬B ∨ ¬C)",
    "(¬A ∨ ¬B ∨ ¬C) ∧ (¬A ∨ ¬B ∨ C) ∧ (¬A ∨ B ∨ ¬C) ∧ (A ∨ B ∨ ¬C) ∧ (A ∨ B ∨ ¬C)",
    "(¬A ∨ B ∨ ¬C) ∧ (A ∨ B ∨ C) ∧ (¬A ∨ B ∨ C) ∧ (A ∨ B ∨ ¬C) ∧ (A ∨ ¬B ∨ C) ∧ (A ∨ ¬B ∨ ¬C)",
    "(¬A ∨ ¬B ∨ ¬C) ∧ (¬A ∨ B ∨ C) ∧ (¬A ∨ ¬B ∨ C) ∧ (A ∨ B ∨ ¬C) ∧ (A ∨ ¬B ∨ C) ∧ (A ∨ B ∨ C) ∧ (¬A ∨ B ∨ ¬C)",
    "(¬A ∨ B ∨ C) ∧ (A ∨ B ∨ ¬C) ∧ (A ∨ ¬B ∨ C) ∧ (A ∨ ¬B ∨ ¬C) ∧ (¬A ∨ ¬B ∨ C) ∧ (¬A ∨ B ∨ ¬C) ∧ (A ∨ B ∨ ¬C) ∧ (A ∨ B ∨ C)",
    "(¬A ∨ ¬B ∨ ¬C) ∧ (¬A ∨ ¬B ∨ ¬C) ∧ (¬A ∨ ¬B ∨ ¬C) ∧ (¬A ∨ ¬B ∨ ¬C) ∧ (A ∨ B ∨ C) ∧ (A ∨ ¬B ∨ ¬C) ∧ (A ∨ B ∨ C) ∧ (A ∨ B ∨ ¬C) ∧ (A ∨ B ∨ ¬C)",
    "(¬A ∨ ¬B ∨ ¬C) ∧ (A ∨ B ∨ ¬C) ∧ (A ∨ B ∨ ¬C) ∧ (A ∨ ¬B ∨ C) ∧ (¬A ∨ B ∨ ¬C) ∧ (¬A ∨ ¬B ∨ C) ∧ (¬A ∨ B ∨ C) ∧ (A ∨ ¬B ∨ C) ∧ (A ∨ B ∨ ¬C) ∧ (¬A ∨ B ∨ ¬C)"
]

matrizCombinations = [
    [False, False, False],
    [False, False, True],
    [False, True, False],
    [False, True, True], 
    [True, False, False],
    [True, False, True],
    [True, True, False],
    [True, True, True]
]

def request_Expression():
    global clausula
    global listLiterales
    global listLetras
    clausula = input("Entrada: ")
    clausula = clausula.replace(" ", "")
    clausula = clausula.upper()

    listLiterales = []

    for i in range(len(clausula)):
        letter = clausula[i]

        if letter != "(" and letter != ")" and letter != "∨" and letter != "V" and letter != "∧" and letter != "¬" and letter not in abecedario:
            print("ERROR: Expresión ingresada no apta para procesar. Vuelva a intentarlo.")
            listLetras.clear()
            listLiterales.clear()
            clausula = ""
            return False
        elif letter in abecedario and letter not in listLiterales:
            listLiterales.append(letter)
        
        if letter in abecedario:
                listLetras.append(letter)

    if len(listLiterales) > 3:
        print("ERROR: La expresión tiene más letras de las permitidas. Vuelva a intentarlo.")
        listLetras.clear()
        listLiterales.clear()
        return False

    j = 0  
    while j + 3 < len(listLetras):
        if listLetras[j] != listLetras[j+3]:
            print("ERROR: El orden de las letras es incorrecta. Vuelva a intentarlo.")
            listLetras.clear()
            listLiterales.clear()
            return False
        j += 1


def prepare_expression():
    global listclausulas
    global clausula
    global counter
    letter = ""
    listClausala = []

    for i in range(len(clausula)):
        counter += 1
        letter = clausula[i]
        if letter != "(" and letter != "∨" and letter != "V" and letter != "∧":
            if letter != ")":
                listClausala.append(letter)
            else:
                listClausulas.append(listClausala[:])
                listClausala.clear()


def change_values():
    global columMatriz
    global listLiterales
    global counter
    prepare_expression()

    for i in range(len(listClausulas)):
        counter += 1
        for j in range(len(listClausulas[i])):
            counter += 1
            if i == 0 and listClausulas[i][j] != "¬":
                listLiterales.append(listClausulas[i][j])

            if listClausulas[i][j] != "¬" and columMatriz < 3:    
                listClausulas[i][j] = matrizCombinations[rowMatriz][columMatriz]
                columMatriz += 1
                
        columMatriz = 0

    for i in range(len(listClausulas)):
        counter += 1
        j = 0
        while j < len(listClausulas[i]):
            counter += 1
            if listClausulas[i][j] == "¬":
                listClausulas[i][j+1] = not(listClausulas[i][j+1])
                listClausulas[i].pop(j)
            j += 1


def find_combination(): 
    global startTime
    global rowMatriz
    global listClausulas
    global listLiterales
    global listLetras
    global counter
    global listaResultados

    if rowMatriz == 0:
        startTime = time.time()

    change_values()
    finalResult = False

    for i in range(len(listClausulas)):
        counter += 1
        boolValue = listClausulas[i][0] or listClausulas[i][1] or listClausulas[i][2]
        if i == 0:
            finalResult = boolValue
        else:
            finalResult = finalResult and boolValue
    
    if finalResult != True and rowMatriz + 1 < 8:
        rowMatriz += 1
        listClausulas = []
        listLiterales = []
        listLetras = []
        find_combination()
        return
    elif rowMatriz == 8:
        listaResultados.append("Flase")
        print("No (Asignación: No hay)")
    else:
        listaResultados.append("True")
        print("Iteraciones: ", counter)
        print("Sí (Asignación: ", 
              listLiterales[0], " = ", matrizCombinations[rowMatriz][0], ", ",
              listLiterales[1], " = ", matrizCombinations[rowMatriz][1], ", ",
              listLiterales[2], " = ", matrizCombinations[rowMatriz][2], ")")

def prueba_conjuntos():
    global listaConjuntosP
    global listTimes
    global listIteraciones
    global clausula
    global rowMatriz
    global columMatriz

    global counter
    global listClausulas
    global listLiterales
    global listLetras

    for i in range(len(listaConjuntosP)):
        clausula = listaConjuntosP[i]
        clausula = clausula.replace(" ", "")
        clausula = clausula.upper()

        execution_time = timeit.timeit(lambda: find_combination(), number=1)
        listTimes.append(execution_time)
        listIteraciones.append(counter)

        counter = 0
        rowMatriz = 0
        columMatriz = 0
        listClausulas = []
        listLiterales = []
        listLetras = []


# bandera = request_Expression()
# while bandera != True:
#     bandera = request_Expression()
# find_combination()

def table_data():
    global listIteraciones
    global listTimes
    global listaResultados

    # Se agrupan los datos a mostrar con su correspondiente de cada lista
    canttidadClausulas = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    datosMostrar = list(zip(canttidadClausulas, listaResultados, listIteraciones, listTimes))

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

def graphic_iterations():
    global listIteraciones

    # Datos a mostrar en el gráfico (x = Cantidad de cláusulas, y = iteraciones)
    x = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    y = listIteraciones

    # Crear el gráfico
    plt.plot(x, y, label='Iteraciones realizadas')

    # Agregar etiquetas y título
    plt.xlabel('Cantidad de cláusulas')
    plt.ylabel('Cantidad de iteraciones realizadas')
    plt.title('Gráfico de las Iteraciones realizadas en los Conjuntos Prueba')

    # Agregar leyenda
    plt.legend()

    # Mostrar el gráfico
    plt.show()

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

prueba_conjuntos()
# table_data()

#graphic_iterations()
graphic_time()