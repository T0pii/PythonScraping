class SkiPlanet:
  def __init__(self, baseUrl, uri, nbPage):
    self.baseUrl = baseUrl
    self.uri = uri
    self.nbPage = nbPage
    self.urls = []
    self.finalFileNameFields = ["title","domain","mountain","minALtitude","maxAltitude","cost"]
  
  def getLinks(self):
    for i in range(1, self.nbPage + 1):
      self.urls.append(self.baseUrl + self.uri + "&pg=" + str(i))
    return self.urls

  def setEndpoints(self, soup):
    div = soup.find('div', {'class': 'conteneur_encadres_residences'})
    divs = soup.findAll('div', {'class': 'encadre_residence_titre_nom'})
    for div in divs:
      a = div.find('a')
      try:
        self.endpoints.extend(a["href"])
      except:
        pass
    return self.setEndpoints
  
  def getEndpoints(self):
    return self.getEndpoints

  def getFinalFieldnames(self):
    return self.finalFieldNames
  
  def getResult(self):
    return self.result
  
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
      
  def getDictResult(self):
    result = []
    for res in self.getResult():
        result.append(res.getDictEntry())
    return result