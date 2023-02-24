import requests
from bs4 import BeautifulSoup
from Toolkit import Toolkit


class Scraper:
    def __init__(self, ScrapInstance, endpointsFile, finalFile):
        self.setScrapInstance(ScrapInstance)
        self.setEndpointsFile(endpointsFile)
        self.setFinalFile(finalFile)
        self.finalFileFieldnames = self.ScrapInstance.getfinalFileFieldnames()
        self.endpointsFileFieldnames = ["id", "link"]

    def setScrapInstance(self, instance):
        self.ScrapInstance = instance
        return self

    def setEndpointsFile(self, filePath):
        self.endpointsFile = filePath
        return self

    def setFinalFile(self, filePath):
        self.finalFile = filePath
        return self

    def soup(self, url, process):
        response = requests.get(url)
        if response.ok:
            soup = BeautifulSoup(response.text, "html.parser")
            return process(soup)
        return

    def soupMultiple(self, urls, process):
        result = []
        for url in urls:
            soup = self.soup(url, process)
        if hasattr(soup, "__len__"):
            result.extend(soup)
        else:
            result.append(soup)
        return result

    def exec(self):
        self.soupMultiple(
            self.ScrapInstance.getLinks(), self.ScrapInstance.setEndpoints
        )
        i = 0
        rows = []
        for url in self.ScrapInstance.getEndpoints():
            row = {}
            row["link"] = url
            row["id"] = i
            i += 1
            rows.append(row)
        Toolkit.fileWriter(self.endpointsFile, self.endpointsFileFieldnames, rows)
        self.soupMultiple(
            self.ScrapInstance.getEndpoints(), self.ScrapInstance.getInfoByPage
        )
        Toolkit.fileWriter(
            self.finalFile, self.finalFileFieldnames, self.ScrapInstance.getDictResult()
        )