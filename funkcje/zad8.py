def bold(func):
    def wrapper(*args, **kwargs):
        wynik = func(*args, **kwargs)
        return "<b>" + wynik + "<\\b>"
    return wrapper

def italic(func):
    def wrapper(*args, **kwargs):
        wynik = func(*args, **kwargs)
        return "<i>" + wynik + "<\\i>"
    return wrapper

@italic
@bold
def funkcja():
    return "jakas funkcja"

print(funkcja())