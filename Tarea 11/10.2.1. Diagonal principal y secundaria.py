'''
Clase:        Fase de fortalecimiento lógico 10
Tema:         Manejo de matrices
Ejercicio:    10.2.1. Diagonal principal y secundaria
Descripción:  

Dada una matriz cuadrada ingresada por el
usuario, crea dos listas, una con los
elementos de la diagonal principal y la otra
con los elementos de la diagonal
secundaria.
Entrada:
• Numero entero N con la dimensión de la
matriz. N conjuntos de números enteros
separados por coma.
Salida:
• Dos listas, una con los elementos de la
diagonal principal y la otra con los
elementos de la diagonal secundaria.



Autor:        Edwin Eduardo Hernandez Lopez
Fecha:        2025-06-13
Estado:       Terminado
'''


Datos = int(input('Ingrese la longitud de la matriz: '))

diagonal = []
diagonalinv = []
matriz = []

for i in range(Datos):
  raw_input = input()
  temp_matriz = list(map(int, raw_input.split(",")))
  matriz.append(temp_matriz)


for i in range(Datos):
  diagonal.append(matriz[i][i])


for i in range(Datos):
  diagonalinv.append(matriz[i][Datos - 1 - i])
print(diagonal)
print(diagonalinv)
