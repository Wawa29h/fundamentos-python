#random.randint()
import random


'''
Clase:        Fase de fortalecimiento lógico 05
Tema:         bloque for
Ejercicio:    5.4.1. ¡Adivina el número
Descripción:  

5.4.2. Sumador de valores posicionales
Descripción:  Genera un número aleatorio entre 1 y 100 y pide al usuario que lo adivine.
El programa debe seguir pidiendo números hasta que acierte. En cada
intento fallido el programa notificará al usuario si el número secreto es
mayor o menor al último valor ingresado.

Autor:        Edwin Eduardo Hernandez Lopez
Fecha:        2025-05-30
Estado:       Terminado
'''

NumeroSecreto = random.randint(1, 100)
  

while True:
    Numeros = input('Ingresa un numero entre 1 y 100:')

    if int(Numeros) == int(NumeroSecreto):
      print('Encontraste el numero')
      print('fin del juego')
      break
    elif int(Numeros) > int(NumeroSecreto):
      print('El numero secreto es menor')
    else:
      print('El numero secreto es mayor')







