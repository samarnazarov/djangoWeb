from django.contrib import admin
from .models import Workers, FreeMessage


@admin.register(Workers)
class WorkersAdmin(admin.ModelAdmin):
    list_display = ['username','tabelnumber','fullname','shortname','photo','phone']
    list_filter = ['fullname','tabelnumber']

admin.site.register(FreeMessage)
