from django.contrib import admin

from .models import LogEvent


@admin.register(LogEvent)
class LogEventAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'computer_name', 'event_type', 'application', 'window_title')
    search_fields = ('computer_name', 'event_type', 'application')
    list_filter = ('event_type', 'application')
