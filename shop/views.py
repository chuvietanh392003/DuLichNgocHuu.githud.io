from django.shortcuts import render, redirect

def home(request):
    return render(request, 'home.html')

def trend(request):
    return render(request, 'pages/trend.html')
def price(request):
    return render(request, 'pages/price.html')
def inbox(request):
    return render(request, 'pages/inbox.html')

def book_ticket(request):
    if request.method == 'POST':
        redirect('home')
    return render(request, 'pages/book_ticket.html')

