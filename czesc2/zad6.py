liczby = [5, 2, 1, 4, 3]
indeks = [0, 1, 2 , 3, 4]
#assert False

min_ = liczby[0]
max_ = liczby[0]

for x in liczby:
    if x < min_:
        min_ = x
    if x > max_:
       max_ = x

print(min_, max_)
print(liczby.index(min_), liczby.index(max_))

liczby[liczby.index(min_)] = max_
liczby[liczby.index(max_)] = min_

liczby[liczby.index(min_)], liczby[liczby.index(max_)] = max_, min_

print(liczby)

#assert liczby == [1, 2, 5, 4, 3]
#for i in range(len(liczby)):
#    if min
#    print(liczby[i])

#assert True

#liczby = [1, 2, 5, 4, 3]