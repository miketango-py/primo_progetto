from django.contrib import admin
from .models import Autore, Genere, Libro
# Register your models here.
# superuser e password= maurospinarelli

admin.site.register(Autore)
admin.site.register(Genere)
admin.site.register(Libro)
