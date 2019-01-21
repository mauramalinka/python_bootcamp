from threading import Thread
from urllib.request import urlopen
from time import time


przed = time()
for i in range(10):
    with urlopen(f"https://www.metaweather.com/api/location/search/?query=Warsaw") as file:
        print(file.read())
po=time()
#watkami
ile = po - przed

print(f"Zajeło to {ile}s")

print(f"Teraz zaczynam rownolegle")

przed = time()
class MyThread(Thread):

    def run(self):
        with urlopen(f"https://www.metaweather.com/api/location/search/?query=Warsaw") as file:
            print(file.read())


watki = []

for i in range(10):
    watek = MyThread()
    watek.start()
    watki.append(watek)

for watek in watki:
    watek.join()

po=time()

ile = po - przed

print(f"Zajeło to {ile}s")