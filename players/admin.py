# admin.py
from django.contrib import admin
from .models import Sport, Player, PlayerStat

# Register models for the admin interface
admin.site.register(Sport)
admin.site.register(Player)
admin.site.register(PlayerStat)
