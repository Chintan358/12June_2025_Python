import requests
import json

lat = 30.0225
lng = 80.5714

url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lng}&appid=9f6c443e9f248d8b6c3dd954f194f35f&units=metric"

resp = requests.get(url)

data = resp.json()
temp = data['main']['temp']
pressure = data['main']['pressure']
humidity = data['main']['humidity']
city = data['name']

print(f"""
city  : {city}
temp  : {temp}
pressure  : {pressure}
Humidity : {humidity}

""")
