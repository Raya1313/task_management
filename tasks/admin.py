from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title', 'created_at', 'updated_at')
    date_hierarchy = 'created_at'
    list_filter = ['is_completed', 'created_at']
    show_facets = admin.ShowFacets.ALWAYS
