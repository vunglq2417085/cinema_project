from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.movie_list_view, name='movie_list'),
    path('movie/<int:id>/',views.movie_detail_view,name = 'movie_detail'),
    path('booking/<int:showtime_id>/',views.seat_selection,name='seat_selection'),
    path('booking/success/<int:ticket_id>/', views.booking_success, name='booking_success'),
    path('my-tickets/', views.my_tickets_view, name='my_tickets'),
]