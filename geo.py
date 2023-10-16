import requests

url = "https://us1.locationiq.com/v1/search.php"

city = input("Introduce tu ciudad : ")


token = "pk.5df39ce223f61fa5ba9ccf6b1e896a61"

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