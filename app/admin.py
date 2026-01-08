from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register((SiteContactInfo, RestourantInfo,  Admin, Chef_category, Chef_rewards, EventCategory, SpecialEvents, RestourantMedia, Category, BusinessHours, OperationHours, NormalHours),)

@admin.register(Dishes)
class DishesAdmin(admin.ModelAdmin):
    search_fields = ('name', 'desc')
    list_display = ('name', 'price', 'chef_choices')
    list_filter = ('chef_choices',)
    ordering = ('name', 'price')

@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'nickname')
    search_fields = ('name', 'nickname', 'text')

@admin.register(Chef)
class ChefAdmin(admin.ModelAdmin):
    list_display = ('name', 'main_chef')
    list_filter = ('main_chef',)
    search_fields = ('name',)

@admin.register(Chef_pick_dish)
class ChefPickDishAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name', 'desc')

@admin.register(BookTable)
class BookTableAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'date', 'time', 'guest_choice')
    list_filter = ('date',)
    search_fields = ('name', 'phone')

@admin.register(BookBusinessTable)
class BookBusinessTableAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'date', 'time', 'occasions')
    list_filter = ('occasions', 'date')

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'from_date', 'to_date')
    ordering = ('-from_date',)

