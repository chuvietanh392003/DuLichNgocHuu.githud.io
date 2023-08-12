from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def trend(request):
    return render(request, 'pages/trend.html')

def trend(request):
    return render(request, 'pages/book_ticket.html')

