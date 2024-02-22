import requests
import json
import folium

position = requests.get("http://api.open-notify.org/iss-now.json")
personnes = requests.get("http://api.open-notify.org/astros.json")

people=[]
for k in personnes.json()["people"]:
    people.append(k["name"])

personnes_tableau=""
for k in people:
    personnes_tableau+="<li>"+k+"</li>"

latitude=position.json()["iss_position"]["latitude"]
longitude=position.json()["iss_position"]["longitude"]
zoom=1
#création de la carte en lui passant la latitude et la longitude et le zoom
carte = folium.Map( zoom_start=zoom,location=[latitude, longitude], width=1000, height=500)
#création d'un cercle à la position souhaitée
codeHTMLpopUp="<p style='text-align:center;width:150px'>ISS<br>Latitude : "+str(latitude)+"<br>Longitude : "+str(longitude)+"</p>""<ul>"+personnes_tableau+"</ul>"
folium.CircleMarker(
    location=[latitude, longitude],
    radius=10,
    popup=codeHTMLpopUp,
    color="#000000",
    fill=True,
    fill_color="#ff0000",
    ).add_to(carte)
#dans eduPython on enregistre la carte qu'on ouvrira dans un navigateur
carte.save("carteISS.html")
#dans notebook, on affiche directement la carte
#carte