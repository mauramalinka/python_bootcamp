import sys
import os
i = 0

def tree(katalog, i):
    numb = list(os.scandir(katalog))
    for element in numb:
        print(i * "|    ", element.name, sep = "")
        if element == numb[-1]:
            print(i * "_    ", element.name, sep="")
        else:
            tree(element, i + 1)



directory=sys.argv[1]
tree(directory, 0)

