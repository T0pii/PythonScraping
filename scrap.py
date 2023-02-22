import requests
from bs4 import BeautifulSoup
import csv

baseUrl = 'https://www.ski-planet.com/fr'
uri = '/reservation/online_affiche.php?DteFrom=&NbNuits=&formule=false|false|false&MassifID=&DptID=&StationID=&TypeLog=&Nbpers=6'

def getEndpoints(soup):
  links=[]
  div = soup.find('div', {'class': 'conteneur_encadres_residences'})
  divs = soup.findAll('div', {'class': 'encadre_residence_titre_nom'})
  for div in divs:
    a = div.find('a')
    links.append(a["href"])
  return links

def getInfoByPage(soup):
  domaine = soup.find('div', {'class' : 'domaine'}).getText().replace("Domaine ",'')
  altitude = soup.find('div', {'class' : 'pistes'}).getText().replace("Altitude ", '')
  avis = soup.find('span', {'class' : 'note'}).getText().replace('/10','')
  infos = {
    "domaine" : domaine,
    "altitude" : altitude,
    "avis" : avis
  }
  return infos

def getSoup(url, process):
  response = requests.get(url)
  if response.ok:
    soup = BeautifulSoup(response.text, 'html.parser') 
    return process(soup)
  return []

def fileWriter(file, fieldnames, data):
  result = []
  with open(file, 'w', encoding="UTF8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for d in data:
      writer.writerow(d)

"""soup = BeautifulSoup(requests.get("https://www.ski-planet.com/fr/location-ski/residence-appart-vacances-pyrenees-2000_pyrenees-2000.html").text, 'html.parser') 
print(soup.findAll('div',{'class': 'bloc-bandeau'}))
"""

endpoints = getSoup(baseUrl + uri, getEndpoints)

endpointsDict = []
for endpoint in endpointsDict:
  endpointsDict.append({"link" : endpoint})

allResults = []
for endpoint in endpoints:
  allResults.append(getSoup(endpoint, getInfoByPage))

print(allResults)
fileWriter('links.csv',['link'],endpointsDict)