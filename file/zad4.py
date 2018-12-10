import os

path = 'C:/Users/kurs/PycharmProjects/python_bootcamp/file/'

for path, dirs, files in os.walk(path):
  print(path)
  for f in files:
    print(f'\t{f}')
