from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.welcomepage),
    path('movie/add', views.movieadd),
    path('cast/add', views.castadd),
    path('cast/show', views.castshow),
    path('movie/show', views.movieshow),
]