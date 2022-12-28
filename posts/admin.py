from django.contrib import admin
from .models import Item


class AdminItem(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')

admin.site.register(Item, AdminItem)