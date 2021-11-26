import random
import csv

nregistros=int(input("Ingreso el numero de registros a generar: "))
valmax=int(input("valor numerico maximo a generar en las columnas: "))

#for row in csv.reader(open('C:/Users/Alex Zárate/Desktop/Alex Zárate 2021/Uni 2021 - B/Reconocimiento de Patrones Sintáctico Estructural/ReconociemientoPatrones/bdmatutino.csv')):
 #   Tejido.objects.create(**dict(zip(fields, row)))

import csv
from home.models import Tejido
fields = ['temperatura', 'color', 'inflammation']
for row in csv.reader(open('bdmatutino.csv')):
    Tejido.objects.create(**dict(zip(fields, row)))

with open('bdmatutino.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for i in range(0,nregistros):
        texto= [random.randint(0, valmax), random.randint(0, valmax), random.randint(0, valmax)]
        writer.writerow(texto)