from bs4 import BeautifulSoup
import requests

URL = "https://dining.missouri.edu/locations/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
openhalls = (soup.find("table"))

halls = ["1+5+3 Salads and Soups", "1839 Kitchen", "Baja Grill", "Bookmark Café", 
        "Catalyst Café", "Do Mundo's", "Emporium Café", "infusion", "Legacy Grill",
        "Mort's", "Olive & Oil", "Panda Express", "Plaza 900 Dining", "Potential Energy Café", "Pizza & MO",
        "Breakfast & MO", "Sabai", "Starbucks - Memorial Union", "Starbucks - Southwest",
        "Subway - Hitt Street", "Subway - Southwest", "Sunshine Sushi", "The MARK on 5th Street",
        "Tiger Avenue Deli", "Truffles", "Wheatstone Bistro"]

dictopenhalls = {}
for hall in halls:
    dictopenhalls[hall] = hall in openhalls.text

allopenhalls = []
for hall in dictopenhalls:
    if dictopenhalls[hall]:
        allopenhalls.append(hall)
allopenhalls.append(" FakeHall")


openhalls = (openhalls.text).replace("\n", "").replace("\t", "").replace("  ", "")
openhalls += " FakeHall"
openhallstimesdict = {}
for hall in range(len(allopenhalls)-1):
    openhallstimesdict[allopenhalls[hall]] = openhalls[openhalls.find(allopenhalls[hall])+len(allopenhalls[hall]):openhalls.find(allopenhalls[hall+1])].strip()

allhallstimes = {}

for hall in halls:
    if hall in openhallstimesdict:
        allhallstimes[hall] = openhallstimesdict[hall].replace("Breakfast", "").replace("Dinner", ", ").replace("Lunch", ", ")
    else:
        allhallstimes[hall] = "CLOSED"

def getAllDiningHallTimesDay():
    return((soup.find_all("th"))[1].text)
    
def getAllDiningHallTimes():
    return allhallstimes