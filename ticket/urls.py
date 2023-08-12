from django.urls import path
from . import views


urlpatterns = [
    path('add_ticket', views.add_ticket, name='add_ticket'), 
]