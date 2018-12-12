import re # regular expression


test_kod = re.compile("\d{2}-\d{3}")
test_email = re.compile("\w+@\w+\.[a-z]+")
test_db= re.compile("[0-3]*[0-9]\s[A-Z][a-z]{2}\s[1-9][0-9]{2,3}")

wynik = regex.findall("01-346")

print(wynik)