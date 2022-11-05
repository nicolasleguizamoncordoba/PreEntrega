from django.contrib import admin

# Register your models here.
from appcoderhouse.models import Alumno, Profesor, Curso

admin.site.register(Alumno)
admin.site.register(Profesor)
admin.site.register(Curso)
