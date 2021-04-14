from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.welcomepage),
    path('movie/add', views.movieadd),
    path('cast/add', views.castadd),
    path('cast/show', views.castshow),
    path('movie/show', views.movieshow),
    path('cast/edit/<int:id>', views.castedit),
    path('cast/update/<int:id>', views.castupdate),
    path('cast/delete/<int:id>', views.castdelete),
    path('movie/delete/<int:id>', views.moviedelete),
    path('movie/edit/<int:id>', views.movieedit),
    path('movie/update/<int:id>', views.movieupdate),
]