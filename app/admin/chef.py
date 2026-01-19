from django.contrib import admin
from app.models.chef import Chef, Chef_pick_dish

@admin.register(Chef)
class ChefAdmin(admin.ModelAdmin):
    list_display = ('name', 'main_chef')
    list_filter = ('main_chef',)
    search_fields = ('name',)

@admin.register(Chef_pick_dish)
class ChefPickDishAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name', 'desc')