class SkiPlanetEntry:
  def __init__(self,name,domain,mountain,altitude,note,cost):
    self.name = name
    self.setDomain(domain)
    self.setMountain(mountain)
    self.setAltitude(altitude)
    self.setNote(note)
    self.setCost(cost)

  def setDomain(self, domain):
    self.domain = domain.replace("Domaine ", "")
    
  def setMountain(self, mountain):
    self.mountain = mountain.replace('Massif ', "")

  def setAltitude(self, altitude):
    altitudes = altitude.replace('Altitude ', "").replace('m','').replace(" ", "").split('/')
    self.altitudeMin = altitudes[0]
    self.altitudeMax = altitudes[1]
    
  def setNote(self, note):
    self.note = note.replace("/10", "")
    
  def setCost(self, cost):
    self.cost = cost.replace(" ","").replace("€","")
    
  def getDictEntry(self):
    global id
    return {
      "nom" : self.name,
      "domaine" : self.domain,
      "massif" : self.mountain,
      "min_altitude" : self.altitudeMin,
      "max_altitude" : self.altitudeMax,
      "note" : self.note,
      "prix" : self.cost
    }