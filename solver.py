import numpy as np

# función para leer matriz desde el archivo de texto
def leer_matriz(archivo):
    f = open(archivo,"r")
    M = np.zeros((9,9),dtype=int)
    for i in range(0,9):
        linea = f.readline()
        b = linea.split()
        for j in range (0,9):
            M[i,j] = int(b[j])
    return M

#función para encontrar un cuadro vacío
def vacio(M):
    for i in range(9):
        for j in range(9):
            if M[i,j]==0:
                return (i,j)
    return None

#función para evaluar reglas del sudoku
def condiciones(M,line,col,num):
    if num in M[line]: return False
    if num in M[:,col]: return False
    cuadroFila=3*(line//3)
    cuadroCol=3*(col//3)
    subcuadro = M[cuadroFila:cuadroFila+3, cuadroCol:cuadroCol+3]
    if num in subcuadro: return False
    return True

#resolver usando backtracking
def pruebaSudoku(M):
    espacio = vacio(M)
    if espacio is None: return True
    fila,col = espacio
    for num in range(1,10):
        if condiciones(M,fila,col,num):
            M[fila,col] = num
            if pruebaSudoku(M): return True
            M[fila,col] = 0
    return False
