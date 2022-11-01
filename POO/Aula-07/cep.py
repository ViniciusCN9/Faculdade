import requests
import folium

cep = requests.get("https://cep.awesomeapi.com.br/json/17209420")
cep = cep.json()

latitude = cep['lat']
longitude = cep['lng']


mapa = folium.Map(location=[latitude, longitude],zoom_start=13)

folium.Marker(
    [latitude, longitude], popup="<i>Casa</i>").add_to(mapa)

mapa.save("index.html")
