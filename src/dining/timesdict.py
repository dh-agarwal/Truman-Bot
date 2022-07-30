from bs4 import BeautifulSoup
import requests

def getTimesDict(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    timestable = (((soup.find(class_="textwidget")).text).replace("Date\nHours", "").strip().split("\n\n\n"))

    timesdict = {}

    for day in timestable:
        timesdict[day[:day.find("\n")]] = day[day.find("\n")+1:]

    return timesdict