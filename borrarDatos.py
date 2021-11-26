
import csv
from home.models import Tejido
fields = ['temperatura', 'color', 'inflammation']
for row in csv.reader(open('bdmatutino.csv')):
    Tejido.objects.create(**dict(zip(fields, row)))


from home.models import Tejido
Tejido.objects.get(id__in = range(50,100)).delete()


#Eliminar elementos en un rango del ID
from home.models import Tejido
tejidos = Tejido.objects.all()
for tejido in tejidos[100:300]:
    tejido.delete()