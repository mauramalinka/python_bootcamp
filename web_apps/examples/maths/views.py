from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from maths.models import Math


def calculate(request, dzialanie, a , b):
    a, b = int(a), int(b)

    if dzialanie == 'add':
        c = a + b
    elif dzialanie == 'sub':
        c = a - b
    elif dzialanie == 'div':
        if b == 0:
            c = "Nie dziel przez zero cholero"
        else:
            c = a / b
    elif dzialanie == 'mul':
        c = a * b
    m = Math(calculate=dzialanie, a=a, b=b, c=c)
    m.save()
    return HttpResponse(f"Wynik = {c}")
