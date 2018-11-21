def prosty_dekorator(func):
    def wrapper(*args, **kwargs):
        print("Przed wywołaniem")
        results = func(*args, **kwargs)
        print("Po wywołaniu")
        return results
    return wrapper #zwraca funkcja

def dwa_wywolania(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        results = func(*args, **kwargs)
        return results
    return wrapper #zwraca funkcja

@prosty_dekorator
@dwa_wywolania
def fun():
    print(f"Cześć")

#prosty_prawie_dekorator(fun)

#nowa_fun = prosty_prawie_dekorator(fun)

print("Akuku")
fun()
