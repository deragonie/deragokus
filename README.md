# deragokus
resolvedor de sudokus automatizado mediante backtracking!!

se utilizan matrices de numpy para representar bidimensionalmente a los sudokus a resolver y se utiliza una estrategia de poda para poder encontrar soluciones óptimas a cualquier dificultad de sudokus.

## ¿cómo funciona?
1. el programa lee un archivo de texto con la config inicial del tablero, donde '0' representa las casillas vacías.
2. encuentra una posición vacía
3. intenta colocar una posición del 1 al 9
4. valida que el número propuesto no se repita en la **fila**, **columna** ni **subcuadrícula de 3x3**
5. si el número es válido, avanza de forma recursiva al siguiente espacio, si el camino no tiene solución, se aplica un backtracking y prueba la siguiente opción disponible.

## uso
se necesita tener instaladas las dependencias de numpy, si no se tiene, se puede instalar mediante:
```bash
   pip install numpy
```

luego se puede ejecutar el programa en la terminal mediante
```bash
python main.py
```

el cual te pedirá un nombre de archivo y debes ponerlo completo, por ejemplo, 'sudoku1.txt'

## nota
los sudokus incluidos son de ejemplo, se pueden cambiar
