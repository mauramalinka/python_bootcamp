import json
from urllib.request import urlopen

gdzie = input("Podaj lokalizacje:")

with urlopen(f"https://www.metaweather.com/api/location/search/?query={gdzie}") as file:
    data = json.loads(file.read().decode("utf-8"))
print(data)
woeid = data[0]["woeid"]

with urlopen(f"https://www.metaweather.com/api/location/{woeid}") as f:
    data = json.loads(f.read().decode("utf-8"))



prognozy = data['consolidated_weather']
for element in prognozy:
    print(f"{element['applicable_date']}")
    print(f"{element['the_temp']}")
    print(f"{element['humidity']}\n")

