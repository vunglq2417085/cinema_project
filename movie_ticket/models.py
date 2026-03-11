from django.db import models
from django.conf import settings
# Create your models here.
#movie
class Movie(models.Model):
    title = models.CharField(max_length= 100, verbose_name= "tiêu đề")
    description = models.TextField(null = True,blank= True,verbose_name= "mô tả")
    duration = models.PositiveIntegerField(verbose_name= "thời lượng (phút)")
    poster = models.ImageField(upload_to='posters/',null=True,blank=True,verbose_name="poster")
    def __str__(self):
        return self.title

#room
class Room(models.Model):
    name = models.CharField(max_length= 5,verbose_name="số phòng")
    capacity = models.IntegerField(default=50, verbose_name= "sức chứa")
    def __str__(self):
        return self.name
    
#seat
class Seat(models.Model):
    room = models.ForeignKey(Room, related_name = "seats", on_delete = models.CASCADE)
    seat_number = models.CharField(max_length=5,verbose_name="số ghế")
    def __str__(self):
        return f"{self.room} - {self.seat_number}"
    
#showtime
class Showtime(models.Model):
    movie = models.ForeignKey(Movie, related_name= "showtimes",on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_time = models.DateTimeField(verbose_name= "thời gian bắt đầu")
    price = models.DecimalField(max_digits=10,decimal_places= 0, verbose_name= "giá vé")
    def __str__(self):
        return f"{self.movie} - {self.start_time.strftime('%d/%m %H:%M')}"
    
#ticket
class Ticket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)
    showtime = models.ForeignKey(Showtime, on_delete= models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete= models.CASCADE)
    price_at_purchase = models.DecimalField(max_digits= 10,decimal_places= 0, verbose_name= "giá mua")
    created_at = models.TimeField(auto_now_add=True ,verbose_name="mua tại thời điểm")
    class Meta:
        unique_together = ('showtime','seat')
    def __str__(self):
        return f"Vé: {self.user}-{self.showtime.movie.title}"
