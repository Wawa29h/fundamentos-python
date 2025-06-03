'''
Clase:        1. Introducción a NumPy
Tema:        uso de numpy
Ejercicio:    5. Cuestionario de trabajo
Descripción:  

Responde cada pregunta escribiendo el código necesario para obtener la respuesta.
Agrega también comentarios o respuestas escritas cuando se solicite explicación.
No borres las secciones anteriores del archivo python desarrollado para esta guía de trabajo, simplemente agrega tus respuestas al final.
Puedes auxiliarte de tu herramienta IA preferida, pero recuerda las buenas prácticas para su uso. Somos responsables de comprender el resultado.

Salida:
• Las distintas respuestass

Autor:        Edwin Eduardo Hernandez Lopez
Fecha:        2025-06-02
Estado:       Terminado
'''

import numpy as np
consumo = np.array([
    [12.5, 13.2, 11.9, 14.0, 13.5, 15.0, 14.3],
    [10.1, 10.5, 10.0, 11.2, 11.5, 12.0, 11.8],
    [14.0, 14.2, 13.9, 15.5, 15.1, 16.0, 15.8],
    [9.0, 9.2, 8.9, 9.5, 9.8, 10.0, 9.7],
    [16.2, 16.5, 16.0, 17.1, 17.4, 18.0, 17.8],
    [11.0, 11.3, 11.1, 12.0, 12.4, 12.8, 12.5],
    [13.5, 13.8, 13.2, 14.1, 14.6, 15.0, 14.9],
    [10.8, 11.0, 10.6, 11.5, 11.8, 12.2, 12.0],
    [15.1, 15.5, 15.0, 16.0, 16.4, 17.0, 16.7],
    [8.5, 8.7, 8.4, 9.0, 9.2, 9.5, 9.3],
])

#linea por array? y caa columna son los dias,.

#exploracion inicial de datos
print("Dimensiones:", consumo.ndim) #2 filas y columnas
print("forma:", consumo.shape) #10 casasa y 7 dias
print("tipo de datos", consumo.dtype) #son floats duh
print("consumo del primer hogar:", consumo[0])
print("consumo del miercoles(Dia 3):", consumo[:, 2])# Todos los datos de la columna

print("-------------------------Promedios-------------------------------/n")

promedios_por_hogar = np.mean(consumo, axis=1) #promedio de cada fila
print("Promedios por hogar:", promedios_por_hogar)

promedio_por_dia = np.mean(consumo, axis=0) #promedio de cada columna
print("Promedio por día:", promedio_por_dia)

total_consumo = np.sum(consumo)
print("Total de consumo:", total_consumo) #sum suma todos los valres de la matriz

print("-------------------------Maximos-------------------------------")

maximos = np.max(consumo, axis=1) #axis valores mas altos que ocuparon cada semana las casa
print(maximos)

minimos = np.min(consumo, axis=0) #axis valores mas bajos que ocuparon cada semana las casa
print(minimos)

dedsviacion = np.std(consumo) #desviacion estandar, mide cuatno varian los datos depende al promedio
print(dedsviacion)

print("-------------------------Comparaciones-------------------------------")

consumo_total_hogar = np.sum(consumo, axis=1)
print("Consumo total por hogar:", consumo_total_hogar) #suma el consumo de cada hogar de cada dias

hogar_mayor_consumo = np.argmax(consumo_total_hogar)
print("Hogar con mayor consumo:", hogar_mayor_consumo)

#Encuentran la posición (índice) del hogar que consumió más y menos energía en la semana.
#tira el indice /  fila
consumo_menor_hogar = np.argmin(consumo_total_hogar)
print("Hogar con menor consumo:", consumo_menor_hogar)


print("-------------------------Filtro-------------------------------")
#compara cada gohar con un valor a 100
altos = consumo_total_hogar > 100
#filtrando los hogares quee cumples la condicion

consumo_mayor_100 = np.where(altos)[0]
print("Consumo mayor a 100:", consumo_mayor_100)

print("-------------------------Normalizacion de Datos -------------------------------")
#aplicando normalizacion MinMax al conjunto de datos
consumo_normalizado = (consumo- consumo.min()) / (consumo.max() - consumo.min())
print(consumo_normalizado)

print("-------------------------Respuestas de actividad -------------------------------")
'''1. ¿Cuál es el consumo del hogar 5 el viernes (día 5)?
2. Usando indexación, muestra el consumo de los últimos 3 hogares el domingo.
3. Calcula el promedio de consumo los fines de semana (sábado y domingo, columnas 5 y 6).
4. ¿Qué día de la semana tiene la mayor desviación estándar entre hogares? Explica qué indica esto.
5. Identifica los 3 hogares con menor consumo total durante la semana. Muestra sus índices y valores.
6. Si el hogar 3 aumenta su consumo en un 10% cada día, ¿cuál sería su nuevo consumo total semanal?
'''
dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
#1
consumo_casa_5 = consumo[4,4]
print("1. el consumo de la casa 5 durante el viernes es",consumo_casa_5)

#2
ult3hogares = consumo[-3:, 6]
print('2. consumo de los tres ultimos hogares el domingo', ult3hogares)

#3
finde = consumo[:, 5:7]
promedio_finde = np.mean(finde)
promedio_finde_por_dia = np.mean(finde, axis=0)
print("3. Promedio general fin de semana:", promedio_finde)
print("3.1   Promedio sábado:", promedio_finde_por_dia[0])
print("3.2   Promedio domingo:", promedio_finde_por_dia[1])

#4
desviaciones_por_dia = np.std(consumo,axis=0)
mayor_desviacion = np.argmax(desviaciones_por_dia)
print("4.Día con mayor desviación estándar entre hogares:", dias[mayor_desviacion])
#¿Qué día de la semana tiene la mayor desviación estándar entre hogares? Explica qué indica esto.
print("El dia con mayor desviacion estandar indica que humo mas desigualdad o variabilidad en el consumo entre los hogares ese dia.")

#5
consumo_total_hogar = np.sum(consumo, axis=1)
indices_menor_consumo = np.argsort(consumo_total_hogar)[:3]
valores_menor_consumo = consumo_total_hogar[indices_menor_consumo]

print("5.Índices de los 3 hogares con menor consumo:", indices_menor_consumo)
print("5.1 Consumos totales de esos hogares:", valores_menor_consumo)
#6
hogar_3 = consumo[2]
hogar_3_aumentado = [hogar_3[0]]

dias_semana = np.arange(len(hogar_3)) #arrage me devuelve los dias de la semana
hogar_3_aumentado = hogar_3[0] * (1.10) ** dias_semana
total = np.sum(hogar_3_aumentado)
print("6. El aumento en el consumo total de la semana será de", round(total, 2))
