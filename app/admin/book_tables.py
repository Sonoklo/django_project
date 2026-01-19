from django.contrib import admin
from app.models.book_table import BookTable, BookBusinessTable

@admin.register(BookTable)
class BookTableAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'date', 'time', 'guest_choice')
    list_filter = ('date',)
    search_fields = ('name', 'phone')

@admin.register(BookBusinessTable)
class BookBusinessTableAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'date', 'time', 'occasions')
    list_filter = ('occasions', 'date')