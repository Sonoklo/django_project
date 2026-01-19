from django.contrib import admin
from app.models.event import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'from_date', 'to_date')
    ordering = ('-from_date',)