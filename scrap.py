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
  massif = soup.find('div', {'class' : 'massif'}).getText().replace("Massif ",'')
  domaine = soup.find('div', {'class' : 'domaine'}).getText().replace("Domaine ",'')
  altitude = soup.find('div', {'class' : 'pistes'}).getText().replace("Altitude ", '')
  note = soup.find('span', {'class' : 'note'}).getText().replace('/10','')
  infos = {
    "massif" : massif,
    "domaine" : domaine,
    "altitude" : altitude,
    "note" : note
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
  with open(file, 'w+', encoding="UTF8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for d in data:
      writer.writerow(d)

"""soup = BeautifulSoup(requests.get("https://www.ski-planet.com/fr/location-ski/residence-appart-vacances-pyrenees-2000_pyrenees-2000.html").text, 'html.parser') 
print(soup.findAll('div',{'class': 'bloc-bandeau'}))
"""
endpoints = []
for i in range (1,6):
  endpoints.extend(getSoup(baseUrl + uri + "&p=" + str(i), getEndpoints))
print(len(endpoints))

endpointsDict = []
for endpoint in endpoints:
  endpointsDict.append({"link" : endpoint})

allResults = []
for endpoint in endpoints:
  allResults.append(getSoup(endpoint, getInfoByPage))

fileWriter('links.csv',['link'],endpointsDict)
fileWriter('data.csv',['massif','domaine','altitude','note'],allResults)