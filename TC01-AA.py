#import matplotlib
#import matplotlib.pyplot as plt

#Variables Globales
listClausulas = []
listLiterales = []
listLetras = []
abecedario = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

rowMatriz = 0
columMatriz = 0
clausula = ""

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
    global listaLetras
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
            request_Expression()
        elif letter in abecedario and letter not in listLiterales:
            listLiterales.append(letter)
        
        if letter in abecedario:
                listLetras.append(letter)

    if len(listLiterales) > 3:
        print("ERROR: La expresión tiene más letras de las permitidas. Vuelva a intentarlo.")
        listLetras.clear()
        listLiterales.clear()
        request_Expression()

    j = 0  
    while j + 3 < len(listLetras):
        if listLetras[j] != listLetras[j+3]:
            print("ERROR: El orden de las letras es incorrecta. Vuelva a intentarlo.")
            listLetras.clear()
            listLiterales.clear()
            request_Expression()
        j += 1


def prepare_expression():
    global listclausulas
    global clausula
    letter = ""
    listClausala = []

    for i in range(len(clausula)):
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
    prepare_expression()

    for i in range(len(listClausulas)):
        for j in range(len(listClausulas[i])):
            
            if i == 0 and listClausulas[i][j] != "¬":
                listLiterales.append(listClausulas[i][j])

            if listClausulas[i][j] != "¬" and columMatriz < 3:    
                listClausulas[i][j] = matrizCombinations[rowMatriz][columMatriz]
                columMatriz += 1
                
        columMatriz = 0

    for i in range(len(listClausulas)):
        j = 0
        while j < len(listClausulas[i]):
            if listClausulas[i][j] == "¬":
                listClausulas[i][j+1] = not(listClausulas[i][j+1])
                listClausulas[i].pop(j)
            j += 1


def find_combination(): 
    global rowMatriz
    global listClausulas
    global listLiterales

    change_values()
    finalResult = False

    for i in range(len(listClausulas)):
        boolValue = listClausulas[i][0] or listClausulas[i][1] or listClausulas[i][2]
        if i == 0:
            finalResult = boolValue
        else:
            finalResult = finalResult and boolValue
    
    if finalResult != True and rowMatriz < 8:
        rowMatriz += 1
        listClausulas = []
        listLiterales = []
        find_combination()
    elif rowMatriz == 8:
        print("No (Asignación: No hay)")
    else:
        print("Sí (Asignación: ", 
              listLiterales[0], " = ", matrizCombinations[rowMatriz][0], ", ",
              listLiterales[1], " = ", matrizCombinations[rowMatriz][1], ", ",
              listLiterales[2], " = ", matrizCombinations[rowMatriz][2], ")")

request_Expression()
find_combination()