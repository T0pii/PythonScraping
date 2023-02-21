import requests
from bs4 import BeautifulSoup

baseUrl = 'https://www.studyrama.com'
uri = '/megamoteur/recherche?query=cyber&type=E%20F%20O'
response = requests.get(baseUrl + uri)

if response.ok:
  soup = BeautifulSoup(response.text, 'html.parser') 
  
  ul = soup.find('ul',{"class": "results"})
  lis = ul.findAll('li')
  for li in lis:
    a = li.find('a')
    print(baseUrl + a["href"])

print(response.ok)