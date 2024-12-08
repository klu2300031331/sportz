# models.py
from django.db import models

class Sport(models.Model):
    name = models.CharField(max_length=100)  # e.g., Football, Basketball, etc.

    def __str__(self):
        return self.name

class Player(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    team = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)  # ForeignKey to Sport model
    profile_picture = models.URLField()  # URL for player profile image

    def __str__(self):
        return self.name

class PlayerStat(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="stats")
    games_played = models.IntegerField()
    goals = models.IntegerField()
    assists = models.IntegerField()
    points = models.IntegerField()

    def __str__(self):
        return f"{self.player.name} Stats"
