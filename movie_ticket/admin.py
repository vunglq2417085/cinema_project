from django.contrib import admin
from .models import Room,Movie,Seat,Showtime,Ticket
# Register your models here.

admin.site.register(Movie)
admin.site.register(Room)
admin.site.register(Seat)
admin.site.register(Showtime)
admin.site.register(Ticket)