SAMOGLOSKI = "aeiouy"

def generator(napis):
    for litera in napis:
        if litera in SAMOGLOSKI:
            yield litera

for x in generator("ala ma kota"):
    print(x)

