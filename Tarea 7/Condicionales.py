'''
Clase:        Fase de fortalecimiento lógico 02
Tema:         Condicionales
Ejercicio:    2.3.1. Contraseña segura
Descripción:  Solicita una cadena de texto que representa una contraseña, y verifica si la contraseña
cumple con las siguientes condiciones: tener al menos 8 caracteres, un número y una
mayúscula.

Autor:        Edwin Eduardo Hernandez Lopez
Fecha:        2025-05-21
Estado:       Terminado
'''

contra = 'HolaAmigos123'

mayus = False
num = False

print(mayus)
print(num)

for caracter in contra:
  if caracter.isupper():
    mayus = True
  elif caracter.isdigit():
    num = True

  print(caracter)

print(mayus)
print(num)
if mayus == True and num == True and len(contra) >= 8:
  print('contraseña valida')
else:
  print('contraseña invalida')


  '''
Clase:        Fase de fortalecimiento lógico 02
Tema:         Condicionales
Ejercicio:    22.3.2. Cálculo de impuesto
Descripción:  Desarrollar un programa en Python que permita calcular el impuesto que debe pagar
un usuario por el consumo de energía. El cálculo debe realizarse basado en la siguiente
tabla.

Autor:        Edwin Eduardo Hernandez Lopez
Fecha:        2025-05-21
Estado:       Terminado
'''

unidades = 101

if unidades <= 100:
  print('no hay impuesto')
elif unidades >= 101 and unidades <= 200:
  print(unidades * 0.5)
elif unidades >= 201 and unidades :
  print(unidades * 0.7)
else:
  print(unidades * 0.9)