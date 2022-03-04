from django.contrib import admin
from .models import item, list

# Register your models here.
@admin.register(item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'urgency_level', 'completed']


@admin.register(list)
class ListAdmin(admin.ModelAdmin):
    list_display = ['name', ]