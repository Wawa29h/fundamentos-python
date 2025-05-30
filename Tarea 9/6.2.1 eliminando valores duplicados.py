'''
Clase:        Clase 9
Tema:         Manejo de lista
Ejercicio:    6.2.1  
Descripción:  Eliminando valores duplicados

Autor:        Edwin Eduardo Hernández López 
Fecha:        2025-05-30
Estado:       [ Terminado ]
'''

x = input('Escribe tus datos')


x = x.split()
aux = []


for i in x:
  if i not in aux:
    aux.append(i)

text = ' '.join(aux)
print(text)