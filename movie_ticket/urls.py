from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.movie_list_view, name='movie_list'),
    path('movie/<int:id>/',views.movie_detail_view,name = 'movie_detail')
]