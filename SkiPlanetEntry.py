class SkiPlanetEntry:
  def __init__(self,title,domain,mountain,altitude,note,cost):
    self.title = title
    self.domain = domain
    self.setMountain(mountain)
    self.setAltitude(altitude)
    self.setNote(note)
    self.cost = cost
    
  def setMountain(self, mountain):
    self.domain= mountain.replace('Domaine ', "")

  def setAltitude(self, altitude):
    altitude = altitude.replace('Altitude ', "").replace('M','').split('/').strip()
    self.altitudeMin = altitude[0]
    self.altitudeMax = altitude[1]
    
  def setNote(self, note):
    self.note = note.replace("/10", "")
    
  def getDictEntry(self):
    return {
      "title" : self.title,
      "domain" : self.domain,
      "mountain" : self.mountain,
      "minAltitude" : self.minAltitude,
      "maxAltitude" : self.maxAltitude,
      "note" : self.note,
      "cost" : self.cost
    }