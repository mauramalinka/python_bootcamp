import os

path = '/home/mauram/PycharmProjects/Python_bootcamp/file/'

for path, dirs, files in os.walk(path):
  print(path)
  for f in files:
    print(f'\t{f}')
