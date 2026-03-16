from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie, Showtime,Ticket, Seat
from django.utils import timezone
from django.contrib.auth.decorators import login_required
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

@login_required
def seat_selection(request, showtime_id):
    showtime = get_object_or_404(Showtime, id = showtime_id)
    seats = Seat.objects.filter(room=showtime.room).order_by('id')
    booked_seat_ids = Ticket.objects.filter(showtime = showtime).values_list('seat_id', flat = True)
    if request.method == 'POST':
        seat_id = request.POST.get('seat_id')
        seat = get_object_or_404(Seat, id = seat_id)
        if not Ticket.objects.filter(showtime=showtime, seat = seat).exists():
            new_ticket = Ticket.objects.create(
                user = request.user,
                showtime = showtime,
                seat = seat,
                price_at_purchase = showtime.price
            )
            return redirect('booking_success',ticket_id=new_ticket.id)
        else:
            return render(request,'movie_ticket/seat_selection.html',{
                'showtime':showtime,'seats':seats,'booked_seat_ids':booked_seat_ids,'error': 'ghế đã có người đặt'
            })
    return render(request, 'movie_ticket/seat_selection.html', {
        'showtime': showtime,
        'seats': seats,
        'booked_seat_ids': booked_seat_ids,
    })
@login_required
def booking_success(request, ticket_id):
    # ticket_id lấy từ URL, đảm bảo đúng vé của user đang đăng nhập
    ticket = get_object_or_404(Ticket, id=ticket_id, user=request.user)
    return render(request, 'movie_ticket/booking_success.html', {'ticket': ticket})
@login_required
def my_tickets_view(request):
    # Lọc tất cả vé của người dùng đang đăng nhập
    tickets = Ticket.objects.filter(user=request.user).order_by('-showtime__start_time')
    return render(request, 'movie_ticket/my_tickets.html', {'tickets': tickets})