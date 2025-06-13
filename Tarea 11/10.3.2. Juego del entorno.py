'''
Clase:        Fase de fortalecimiento lógico 10
Tema:         Manejo de matrices
Ejercicio:    10.3.2. Juego del entorno
Descripción:  

Dada una matriz binaria ingresada por el
usuario, verifica para cada celda de una
matriz binaria cuántos elementos con valor
de 1 hay en las celdas vecinas (arriba, abajo,
izquierda, derecha, diagonales).
Entrada:
• Dos números N,M con la dimensión de la
matriz. N conjuntos de M cantidad de
números enteros separados por coma.
Salida:
• Matriz NxM. Cada celda contiene la suma
de elementos con valor de 1 en las celdas
vecinas .


Autor:        Edwin Eduardo Hernandez Lopez
Fecha:        2025-06-13
Estado:       Terminado
'''

filas = int(input('Ingrese la longitud de las filas: '))
columnas = int(input('Ingrese la longitud de las columnas: '))

matriz = []

for i in range(filas):
    raw_input = input()
    temp_matriz = list(map(int, raw_input.split(",")))
    matriz.append(temp_matriz)

resultado = []

# Recorrer cada celda
for i in range(filas):

    fila_resultado = []

    for j in range(columnas):
      
        conteo = 0
        checki = [i-1, i, i+1]
        checkj = [j-1, j, j+1]
        for ni in checki:
            for nj in checkj:
      #esta parte me ayudo chat gpt -----------------
                if ni == i and nj == j:
                    continue  # no contar la celda actual
                if 0 <= ni < filas and 0 <= nj < columnas:
                    if matriz[ni][nj] == 1:
                        conteo += 1
      #hasta aca me ayudo chat gpt ----------------
        fila_resultado.append(conteo)
    resultado.append(fila_resultado)

# Mostrar la matriz resultado
print("Salida:")
for fila in resultado:
    print(fila)