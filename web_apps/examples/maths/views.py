from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def calculate(request, dzialanie, a , b):
    if dzialanie == 'add':
        c = int(a) + int(b)
    elif dzialanie == 'sub':
        c = int(a) - int(b)
    elif dzialanie == 'div':
        if b == 0:
            c = "Nie dziel przez zero cholero"
        else:
            c = int(a) / int(b)
    elif dzialanie == 'mul':
        c = int(a) * int(b)
    return HttpResponse(f"Wynik = {c}")
