from django.contrib import admin
from .models import curso, Horario, Nota

# Register your models here.

class cursosadmin(admin.ModelAdmin):

    readonly_fields=("created","updated")

admin.site.register(curso, cursosadmin)


class Horarioadmin(admin.ModelAdmin):
 pass
admin.site.register(Horario, Horarioadmin)

class Notasadmin(admin.ModelAdmin):
   pass
admin.site.register(Nota, Notasadmin)