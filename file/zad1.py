import sys

try:
    print(sys.argv)
except IndexError:
    print("Zapomniałeś podać nazwę pliku")


print("ścieżka do pliku to: ", sys.argv[1])

with open(sys.argv[1]) as f:
    #i = 0
    for i, line in enumerate(f):
        print(i, line, end="")
#    i += 1