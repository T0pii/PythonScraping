from Scraper import Scraper
from SkiPlanet import SkiPlanet

baseUrl = 'https://www.ski-planet.com/fr'
uri = "/reservation/online_affiche.php?DteFrom=2024-01-01&p="

studyramaInstance = SkiPlanet(baseUrl, uri, 5)

scraper = Scraper(studyramaInstance, "linksList.csv", "infos.csv")

scraper.exec()

print("Done")

exit()