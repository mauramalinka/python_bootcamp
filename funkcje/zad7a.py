data = [1, 2, 3, 4, 5, 6, 7, 3]

start = lambda x: x > 3
stop = lambda x: x ==6

def przytnij(data, start, stop):
    out = []
    for element in data:
        if start(element):
            out.append(element)
        if stop(element):
            break
    return out

def test_1():
    assert przytnij(data = [1, 2, 3, 4, 5, 6, 7], start = lambda x: x > 3, stop = lambda x: x ==6) == [4,5,6]
    assert przytnij(data=[1, 2, 3, 4, 5, 6, 7, 3], start=lambda x: x > 4, stop=lambda x: x == 5) == [5]