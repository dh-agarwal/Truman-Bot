from bs4 import BeautifulSoup
import requests

def getWeek():
    URL = "https://mizzourec.com/facilities/information/hours/"
    page = requests.get(URL, headers = {'User-agent': 'your bot 0.1'})
    soup = BeautifulSoup(page.content, "html.parser")
    return soup.find("h4").text

def getWeekDictionary():
    URL = "https://mizzourec.com/facilities/information/hours/"
    page = requests.get(URL, headers = {'User-agent': 'your bot 0.1'})
    soup = BeautifulSoup(page.content, "html.parser")
    hourstable = soup.find("tbody", class_="row-hover")
    hourstablestr = ""
    for i in hourstable:
        hourstablestr += str(i)

    timinglist = []
    appendstr = ""
    openflag = ""
    closeflag = ""
    append = False
    for i in range(len(hourstablestr)):
        openflag = hourstablestr[i-4:i]
        closeflag = hourstablestr[i:i+5]
        if (openflag == "<th>" or openflag == "<td>"):
            append = True
        if (closeflag == "</th>" or closeflag == "</td>"):
            timinglist.append(appendstr)
            append = False
            appendstr = ""
        if (append):
            appendstr += hourstablestr[i]

    timingdict = {}
    for box in range(0, len(timinglist)-1, 2):
        timingdict[timinglist[box]] = timinglist[box+1]

    return timingdict

def getDaysDictionary(weekDict):
    daysdictvalues = {
        "MONDAY": 1,
        "TUESDAY": 2,
        "WEDNESDAY": 3,
        "THURSDAY": 4,
        "FRIDAY": 5,
        "SATURDAY": 6,
        "SUNDAY": 7
    }

    numberdaysvalues = {
        1: "MONDAY",
        2: "TUESDAY",
        3: "WEDNESDAY",
        4: "THURSDAY",
        5: "FRIDAY",
        6: "SATURDAY",
        7: "SUNDAY"
    }

    daysdict = {}
    inbetween = []
    for days in weekDict:
        if "-" in days:
            inbetween = days.split("-")
            for i in range(daysdictvalues[inbetween[0]], daysdictvalues[inbetween[1]]+1):
                daysdict[numberdaysvalues[i]] = weekDict[days]
        if "/" in days:
            inbetween = days.split("/")
            daysdict[inbetween[0]] = weekDict[days]
            daysdict[inbetween[1]] = weekDict[days]
        elif days in daysdictvalues:
            daysdict[days] = weekDict[days]

    return daysdict