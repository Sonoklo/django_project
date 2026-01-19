from django.contrib import admin
from app.models.dishes import Dishes

@admin.register(Dishes)
class DishesAdmin(admin.ModelAdmin):
    search_fields = ('name', 'desc')
    list_display = ('name', 'price', 'chef_choices')
    list_filter = ('chef_choices',)
    ordering = ('name', 'price')