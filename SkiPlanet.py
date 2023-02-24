from Toolkit import Toolkit
from SkiPlanetEntry import SkiPlanetEntry

class SkiPlanet:
    def __init__(self, baseUrl, uri, nbPage):
        self.baseUrl = baseUrl
        self.uri = uri
        self.nbPage = nbPage
        self.urls = []
        self.endpoints = []
        self.result = []
        self.finalFileFieldnames = [
            "nom",
            "domaine",
            "massif",
            "min_altitude",
            "max_altitude",
            "note",
            "prix",
        ]

    def getLinks(self):
        for i in range(1, self.nbPage + 1):
            self.urls.append(self.baseUrl + self.uri + str(i))
        return self.urls

    def setEndpoints(self, soup):
        div = soup.find("div", {"class": "conteneur_encadres_residences"})
        divs = soup.findAll("div", {"class": "encadre_residence_titre_nom"})
        for div in divs:
            a = div.find("a")
            try:
                self.endpoints.append(a["href"])
            except:
                pass
        return self.endpoints

    def getEndpoints(self):
        return self.endpoints

    def getfinalFileFieldnames(self):
        return self.finalFileFieldnames

    def getResult(self):
        return self.result

    def getInfoByPage(self, soup):
        # Recuperations des infos souhaitees
        name = Toolkit.tryToCleanOrReturnBlank(soup.find("span", {"class": "courant"}))
        mountain = Toolkit.tryToCleanOrReturnBlank(
            soup.find("div", {"class": "massif"})
        )
        domain = Toolkit.tryToCleanOrReturnBlank(soup.find("div", {"class": "domaine"}))
        altitude = Toolkit.tryToCleanOrReturnBlank(
            soup.find("div", {"class": "pistes"})
        )
        note = Toolkit.tryToCleanOrReturnBlank(soup.find("span", {"class": "note"}))
        cost = Toolkit.tryToCleanOrReturnBlank(soup.find("div", {"class": "prix"}))
        # Si promo présente (prix barré), recuperation du prix en promo uniquement
        if soup.find("span", {"class": "barre"}) is not None:
            cost = cost.split("€")[0]
        info = SkiPlanetEntry(name, domain, mountain, altitude, note, cost)
        self.result.append(info)
        return info

    def getDictResult(self):
        result = []
        for res in self.getResult():
            result.append(res.getDictEntry())
        return result
