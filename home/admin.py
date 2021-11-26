from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
#from sintacticoEstructural.home.models import Tejido ##### Primera forma 
from .models import Paciente, Tejido #######Segunda forma

# Register your models here.

class PacienteAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Paciente, PacienteAdmin)


class TejidoAdmin(admin.ModelAdmin):
    list_display = ('color', 'temperatura', 'inflammation','name')

admin.site.register(Tejido, TejidoAdmin)


