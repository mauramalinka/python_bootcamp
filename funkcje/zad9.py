from time import time

x = time()
def czas(func):
    def wrapper(*args, **kwargs):
        przed_wywołaniem = time()
        wynik = func(*args, **kwargs)
        po_wywolaniu = time()
        print(f"Czas wywolania funkcji: {po_wywolaniu - przed_wywołaniem}")
        return wynik
    return wrapper


def fib(x):
    if x <=1:
        return x
    return fib(x-1) + fib(x - 2)

@czas
def funcyja(x):
    return fib(x)

print(funcyja(35))