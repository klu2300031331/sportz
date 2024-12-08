from django.contrib import admin
from .models import Event

class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'location', 'venue', 'available_seats']
    # Remove 'slug' from prepopulated_fields since we no longer have a 'slug' field
    # prepopulated_fields = {'slug': ('title',)}

admin.site.register(Event, EventAdmin)
