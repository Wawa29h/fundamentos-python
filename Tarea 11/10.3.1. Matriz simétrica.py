'''
Clase:        Fase de fortalecimiento lógico 10
Tema:         Manejo de matrices
Ejercicio:    10.3.1. Matriz simétrica
Descripción:  

Dada una matriz cuadrada ingresada por el
usuario, comprueba si la matriz cuadrada es
simétrica respecto a su diagonal principal.
Entrada:
• Numero entero N con la dimensión de la
matriz. N conjuntos de números enteros
separados por coma.
Salida:
• Una línea con una cadena de texto. “La
matriz es simétrica” si es simétrica; “La
matriz no es simétrica” en caso contrario.


Autor:        Edwin Eduardo Hernandez Lopez
Fecha:        2025-06-13
Estado:       Terminado
'''

Datos = int(input('Ingrese la longitud de la matriz: '))

Simetria = True
matriz = []

for i in range(Datos):
  raw_input = input()
  temp_matriz = list(map(int, raw_input.split(",")))
  matriz.append(temp_matriz)

for i in range(Datos):
    for j in range(Datos):
        if matriz[i][j] != matriz[j][i]:
            Simetria = False
            break
    if not Simetria:
        break

if Simetria:
  print('La matriz es simetrica')
else:
  print('La matriz no es simetrica')

