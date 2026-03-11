from django.shortcuts import render, get_object_or_404
from .models import Movie
from django.utils import timezone
# Create your views here.
def movie_list_view(request):
    all_movies = Movie.objects.all()
    return render(request,'movie_ticket/movie_list.html',{'movies': all_movies})

def movie_detail_view(request, id):
    movie = get_object_or_404(Movie, id = id)
    showtimes = movie.showtimes.filter(start_time__gte=timezone.now()).order_by('start_time')
    return render(request, 'movie_ticket/movie_detail.html',{
        'movie': movie,
        'showtimes': showtimes
    })
