import requests
from bs4 import BeautifulSoup
import csv
"""
from SkiPlanetEntry import SkiPlanetEntry 
from SkiPlanet import SkiPlanet
from Scraper import Scraping
"""

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
  mountain = tryToCleanOrReturnBlank(soup.find('div', {'class' : 'mountain'})).replace('mountain ', '')
  domain = tryToCleanOrReturnBlank(soup.find('div', {'class' : 'domain'})).replace("domain ",'')
  altitude = tryToCleanOrReturnBlank(soup.find('div', {'class' : 'pistes'})).replace("Altitude ",'')
  note = soup.find('span', {'class' : 'note'}).getText().replace('/10','')
  infos.append ({
      "mountain" : mountain,
      "domain" : domain,
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
  
fields = ['mountain','domain','altitude','note']
fileWriter('data.csv', fields, rows)