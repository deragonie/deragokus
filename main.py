import os
from solver import leer_matriz, pruebaSudoku

def menu():
    print("EPIC RESOLVEDOR DE SUDOKUS!1!")

    ruta = "data"
    if os.path.exists(ruta):
        archivos = [f for f in os.listdir(ruta) if f.endswith('.txt')]
        for arch in sorted(archivos):
            print (f" . {arch}")
    else:
        print("ERROR rip: no se encontró la carpeta 'data'")

def main():
    menu()
    nombre = input("ingresa nombre del archivo con el sudoku ")
    ruta = os.path.join("data",nombre)
    print("\n cargando...")
    tablero = leer_matriz(ruta)
    if tablero is not None:
        print(tablero)
        print("solving...")
        if pruebaSudoku(tablero):
            print("\n solución:")
            print(tablero)
        else:
            print("\n no existe solución válida para este sudoku")

main()
