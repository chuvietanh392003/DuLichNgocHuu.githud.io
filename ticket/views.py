from django.shortcuts import render, redirect
from .models import Ticket
# Create your views here.
def add_ticket(request):
    if request.method == 'POST':
        road = request.POST.get('route')
        date = request.POST.get('departure-date')
        space = request.POST.get('car-type')

        # Create a new Ticket instance
        new_ticket = Ticket(road=road, date=date, space=space)
        new_ticket.save()
    return redirect('/')