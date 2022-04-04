from django.urls import path
from . import views
 
urlpatterns=[ 
    path('',views.home,name="HOME"),
    path('summarize/<str:pk1>/<str:pk2>',views.summarize,name="summarizer"),
    path('summarize/<str:pk1>/<str:pk2>',views.summarize,name="summarizer"),
    path('summarize/<str:pk1>/<str:pk2>',views.summarize,name="summarizer"),
    path('summarize/<str:pk1>/<str:pk2>',views.summarize,name="summarizer"),
    path('summarize/<str:pk1>/<str:pk2>',views.summarize,name="summarizer"),
    path('summarize/<str:pk1>/<str:pk2>',views.summarize,name="summarizer"),
    path('summarize/<str:pk1>/<str:pk2>',views.summarize,name="summarizer"),



]