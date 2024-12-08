from django.urls import path
from . import views

urlpatterns = [
    path('events/', views.events, name='events'),
    path('events/<int:event_id>/', views.event_detail, name='event_detail'),
    path('payment/', views.payment, name='payment'),
    path('participate/', views.participate, name='participate'),
    path('events/create_event/', views.create_event, name='create_event'),
]
