# This is a web scraper for U4Ea. Given a list of words, output a list of synonyms.
import requests
from bs4 import BeautifulSoup
listOf = []

for x in listOf:
    URL = "https://www.thesaurus.com/browse/" + x
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="meanings")
    synonyms = results.find_all("a")

    outputString = x.capitalize() + ": "
    counter = 0
    for synonym in synonyms:
        counter += 1
        s = synonym.text
        if counter == 1:
            outputString += s.strip()
        else:
            outputString += ", " + s.strip()

    print(outputString + "\n")
