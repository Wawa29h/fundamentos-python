'''
Clase:        Fase de fortalecimiento lógico
Tema:         operadores arismeticos
Ejercicio:    1.3.1. Automatizando el cálculo de la propina
Descripción:  Pide al usuario el total de una cuenta y el porcentaje de propina
(por ejemplo, 10%, 15%, 20%). Calcula y muestra en pantalla el total
a pagar.

Autor:        Edwin Eduardo Hernandez Lopez
Fecha:        2025-05-21
Estado:       Terminado
'''


total = int(input('Cuanto gastaste?'))

propina = 100 / 10
print(f"total de cuenta {total}$ ")
print(f"total de propina {propina}$ ")
print(f"tienes que pagar un total de{total + propina}$ ")

'''
Clase:        Fase de fortalecimiento lógico
Tema:         Concatenar texto
Ejercicio:    1.3.2. Generador del correo de Key
Descripción:  Solicita al usuario su nombre completo (asume dos nombres y
dos apellidos). Luego, el programa generará, su correo con el
formato:
• primer_nombre.primer_apellido@keyinstitute.edu.sv

Autor:        Edwin Eduardo Hernandez Lopez
Fecha:        2025-05-21
Estado:       Terminado
'''

nombre = input("Cuales son tus nombres?")
apellido = input("Cuales son tus apellidos?")

primer_nombre = nombre.split()[0]
primer_apellido = apellido.split()[0]


print(f"el correo que se debe asignar al usuario ingresado es: {primer_nombre}.{primer_apellido}@keyinstitute.edu.sv")