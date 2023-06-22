from django.db import models

# Create your models here.
class Quizz(models.Model):
    quizz_id = models.CharField(max_length=20)
    quantity = models.IntegerField()

    def __str__(self):
        return self.quizz_id