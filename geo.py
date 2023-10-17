import requests
import os
from dotenv import load_dotenv
load_dotenv()

API_TOKEN = os.getenv('TOKEN')

url = "https://us1.locationiq.com/v1/search.php"

city = input("Introduce tu ciudad : ")


token = API_TOKEN

data = {
    'key': token,
    'q': city,
    'format': 'json'
}

response = requests.get(url, params=data)

latitude = response.json()[0]['lat']
longitude = response.json()[0]['lon']

print(f"Latitud: {latitude}")
print(f"Longitud : {longitude}")
print("Developed with ❤️ by Carlos Calleja Saez")