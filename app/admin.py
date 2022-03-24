from django.contrib import admin
from .models import item, list, Profile

# Register your models here.
@admin.register(item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'urgency_level', 'completed']


@admin.register(list)
class ListAdmin(admin.ModelAdmin):
    list_display = ['name', ]

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'image']

