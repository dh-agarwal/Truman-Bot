from bs4 import BeautifulSoup
from datetime import date
import calendar
import requests

def getName():
    URL = "https://dining.missouri.edu/locations/sabai-summer/"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    txt = soup.find("h2")
    return txt.text

def getText(meal):
    URL = "https://dining.missouri.edu/locations/sabai-summer/"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    my_date = date.today()
    dayOfWeek = calendar.day_name[my_date.weekday()]
    if (meal == "breakfast"):
        collapse = "collapse-layer{}1".format(dayOfWeek)
    if (meal == "lunch"):
        collapse = "collapse-layer{}2".format(dayOfWeek)
    text = soup.find("div", id=collapse).text
    return text

def getFoodDict(text):
    text += "last\n\n"
    fooddict = dict()
    prevstring = ''
    appendstring = ''
    doAppend = False
    numofspaces = 0
    veggie = "NotVeggie"

    for ele in range(0, len(text)-1):
        if ((not text[ele].isspace())):
            doAppend = True
            appendstring += text[ele]
        elif ((text[ele+1].isspace())):
            numofspaces += 1
            if (doAppend):
                if (numofspaces > 25):
                    fooddict[prevstring] = "Veggie"
                prevstring = appendstring.strip()
                fooddict.update({appendstring.strip(): veggie})
                appendstring = ''
                doAppend = False
                veggie = "NotVeggie"
                numofspaces = 0
        else:
            appendstring += ' '
    fooddict.pop("last")

    return fooddict

textbreakfast = getText("breakfast")
textlunch = getText("lunch")

fooddictbreakfast = getFoodDict(textbreakfast)
fooddictlunch = getFoodDict(textlunch)

def getSabaiBreakfast():
    stringlist = "**Breakfast**\n"
    for food in fooddictbreakfast:
      stringlist += "• "
      stringlist += food
      if fooddictbreakfast[food] == "Veggie":
        stringlist += " :herb:"
      stringlist += "\n"
    return stringlist

def getSabaiLunch():
    stringlist = "**Lunch**\n"
    for food in fooddictlunch:
      stringlist += "• "
      stringlist += food
      if fooddictlunch[food] == "Veggie":
        stringlist += " :herb:"
      stringlist += "\n"
    return stringlist