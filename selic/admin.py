from django.contrib import admin
from .models import Selic


class SelicAdmin(admin.ModelAdmin):
    list_display = ['id', 'ano', 'mes', 'valor']


admin.site.register(Selic, SelicAdmin)
