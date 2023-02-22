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
  infosTriees = [soup]
  return infosTriees

def getSoup(url, process):
  response = requests.get(url)
  if response.ok:
    soup = BeautifulSoup(response.text, 'html.parser') 
    return process(soup)
  return []

def fileReader(file):
  result = []
  with open(file, 'r', encoding="UTF8", newline="") as f:
    reader = csv.DictReader(f)
    for line in reader:
      result.append(line)
  return result

def fileWriter(file, fieldnames, data):
  result = []
  with open(file, 'w', encoding="UTF8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)
  return fileReader(file)

data = fileReader("links.csv")

fields =  ['test']
fileWriter('infos.csv', fields, data)
exit()

endpoints = getSoup(baseUrl + uri, getEndpoints)

print(endpoints)

result = []
for endpoint in endpoints:
  result.extend(getSoup(endpoint,getInfoByPage))

print(result)