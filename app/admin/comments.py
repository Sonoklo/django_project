from django.contrib import admin
from app.models.comments import Comments


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'nickname')
    search_fields = ('name', 'nickname', 'text')