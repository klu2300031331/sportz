# views.py
from django.shortcuts import render
from .models import Player, PlayerStat

def player_statistics(request):
    players = Player.objects.all()  # Get all players from the database
    player_stats = PlayerStat.objects.all()  # Get all player statistics

    context = {
        'players': players,
        'player_stats': player_stats
    }

    return render(request, 'player_statistics.html', context)
