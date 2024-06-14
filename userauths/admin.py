from django.contrib import admin
from userauths.models import usuario
# Register your models here.

class useradmin(admin.ModelAdmin):
    list_display = ['username', 'email' ]
    

admin.site.register(usuario, useradmin)