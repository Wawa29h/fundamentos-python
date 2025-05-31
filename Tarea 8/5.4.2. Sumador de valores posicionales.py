'''
Clase:        Fase de fortalecimiento lógico 05
Tema:         bloque for
Ejercicio:    5.4.2. Sumador de valores posicionales
Descripción:Pide un número al usuario y suma sus dígitos hasta que quede un solo dígito. Ejemplo:
Si el usuario ingresa 9875, entonces: 9+8+7+5 = 29 → 2+9 = 11 → 1+1 = 2

Autor:        Edwin Eduardo Hernandez Lopez
Fecha:        2025-05-30
Estado:       Terminado
'''

numero = (input('Ingresa un numero:'))


while int(numero) >= 10:
  if numero != "":
    resultado = []
    for n in numero:
      resultado.append(int(n))

    resultado = sum(resultado)
    print(f"{numero} = {resultado}") 
    numero = str(resultado)