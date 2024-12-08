from django.urls import path
from . import views

urlpatterns = [
    path('', views.live_scores, name='live_scores'),  # The empty string means it matches the root of /live-scores/
]