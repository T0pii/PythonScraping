import requests
from bs4 import BeautifulSoup

baseUrl = 'https://www.ski-planet.com/fr'
uri = '/reservation/online_affiche.php?DteFrom=&NbNuits=&formule=false|false|false&MassifID=&DptID=&StationID=&TypeLog=&Nbpers='
response = requests.get(baseUrl + uri)

if response.ok:
  soup = BeautifulSoup(response.text, 'html.parser') 
  div = soup.find('div', {'class': 'conteneur_encadres_residences'})
  divs = div.findAll('div', {'class': 'encadre_residence_titre_nom'})
  for div in divs:
    a = div.find('a') 
    print(a["href"])