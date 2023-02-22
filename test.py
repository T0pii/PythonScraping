import requests
from bs4 import BeautifulSoup

baseUrl = 'https://www.travelski.com'
uri = '/se-results#packages[]=PFP&e=1&capacity=6'
response = requests.get("https://locations.lastminute.com/se-results#e=167&c[]=320%7C321%7C322%7C323%7C324%7C325%7C326%7C327%7C328%7C329%7C330%7C331%7C332%7C333%7C334%7C335%7C336%7C337%7C338&capacity=6&rc_size=10&rc_start=1")

if response.ok:
  soup = BeautifulSoup(response.text, 'html.parser') 
  div = soup.findAll('div', {'class' : 'col-xs-12 tf-result-product-item'})
  print(div)