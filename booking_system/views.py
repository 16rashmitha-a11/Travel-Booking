from django.shortcuts import render, get_object_or_404, redirect
from .models import Trip, Ticket, Customer
from .forms import TicketBookingForm

# View to display all trips
def trip_list(request):
    trips = Trip.objects.all()
    return render(request, 'booking_system/trip_list.html', {'trips': trips})

# View to display trip details and book a ticket
def trip_detail(request, trip_id):
    trip = get_object_or_404(Trip, id=trip_id)
    form = TicketBookingForm(request.POST or None)
    
    if request.method == 'POST' and form.is_valid():
        ticket = form.save(commit=False)
        ticket.trip = trip
        ticket.total_price = trip.price_per_person
        ticket.save()
        return redirect('booking_system:ticket_detail', ticket_id=ticket.id)
    
    return render(request, 'booking_system/trip_detail.html', {'trip': trip, 'form': form})

# View to show ticket details
def ticket_detail(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    return render(request, 'booking_system/ticket_detail.html', {'ticket': ticket})
