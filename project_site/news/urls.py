from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='news-home'),
    path('entertainment/', views.entertainment, name='news-entertainment'),
    path('health/', views.health, name='news-health'),
    path('science/', views.science, name='news-science'),
    path('sports/', views.sports, name='news-sports'),
    path('technology/', views.technology, name='news-technology'),

]