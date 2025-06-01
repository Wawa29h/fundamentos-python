'''
Clase:        Fase de fortalecimiento lógico 06
Tema:         bManejo ed listas
Ejercicio:    6.3.1. Números líderes
Descripción:  

Un número en una lista es "líder" si es
estrictamente mayor que todos los
elementos a su derecha. Dada una lista de
números ingresada por el usuario, imprime
todos los números líderes.
Entrada:
• La primera línea contiene n enteros a₁, ..., aₙ
(1 ≤ aᵢ ≤ 10⁹)
Salida:
• Una línea con todos los números líderes
en el orden en que aparecen en el arreglo.
12

Autor:        Edwin Eduardo Hernandez Lopez
Fecha:        2025-06-01
Estado:       Terminado
'''
#numbers = [1, 65, 1, 1, 16, 5, 6, 8, 6, 4] input de clase
numbers = (input('Ingresa los numeros separados por espacio'))
numbers = list(map(int, numbers.split()))
aux = []

for i in range(len(numbers)- 1):
    if numbers[i] > max(numbers[i+1:]):
        aux.append(numbers[i])
        


print(' '.join(str(x) for x in aux))