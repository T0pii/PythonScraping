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
  infos = []
  massif = tryToCleanOrReturnBlank(soup.find('div', {'class' : 'massif'})).replace('Massif ', '')
  domaine = tryToCleanOrReturnBlank(soup.find('div', {'class' : 'domaine'})).replace("Domaine ",'')
  altitude = tryToCleanOrReturnBlank(soup.find('div', {'class' : 'pistes'})).replace("Altitude ",'')
  note = soup.find('span', {'class' : 'note'}).getText().replace('/10','')
  infos.append ({
      "massif" : massif,
      "domaine" : domaine,
      "altitude" : altitude,
      "note" : note
    })
  return infos

def tryToCleanOrReturnBlank(str):
  try:
    result = str.getText().strip()
  except:
    result = ''
  return result

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

def fileReader(file):
  result = []
  with open(file, 'r', encoding="UTF8", newline="") as f:
    reader = csv.DictReader(f)
    for line in reader:
      result.append(line) 
  return result

endpoints = []
for i in range (1,3):
  endpoints.extend(getSoup(baseUrl + uri + "&p=" + str(i), getEndpoints))
print(len(endpoints))

rows = []
fields = ['link']
for endpoint in endpoints:
  row = {}
  row['link'] = endpoint
  rows.append(row)

fileWriter('links.csv',fields,rows)

rows = []
for link in fileReader('links.csv'):
  rows.extend(getSoup(link['link'], getInfoByPage))
  
fields = ['massif','domaine','altitude','note']
fileWriter('data.csv', fields, rows)