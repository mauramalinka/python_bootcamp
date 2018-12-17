from django.db import models

# Create your models here.
class Math (models.Model):
    calculate = models.CharField(max_length=4) #pierwsza kolumna
    a = models.IntegerField()
    b = models.IntegerField()
    c = models.TextField()
    created = models.DateTimeField(auto_now=True)
