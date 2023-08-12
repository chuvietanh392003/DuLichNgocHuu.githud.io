from django.db import models

# Create your models here.
class Ticket(models.Model):
    road = models.CharField(max_length=200)
    space = models.CharField(max_length=200)
    date = models.DateField()
    def __str__(self):
        return f"Ticket {self.id} - {self.road}, {self.space} ({self.date})"

