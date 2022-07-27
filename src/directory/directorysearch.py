from bs4 import BeautifulSoup
import requests
import src.directory.Person as Person

def getPersonWithSoup(soup):
    keywords = ["Email:", "Title:", "Department:", "Phone:", "Address:", "City:", "State:"]
    person = Person.Person("", "", "", "", "", "", "", "")
    personinfotext = (soup.find("p", {"class": "miz-card__text"}).text)
    if ("\n\n" in personinfotext):
        personinfotext = personinfotext[:personinfotext.index("\n\n")]
    person.name = (soup.find("h2", {"class": "miz-card__title miz-card__title--mark miz-card__title--news miz-graphik"}).text)
    personinfolist = (personinfotext.split())
    for item in range(len(personinfolist)-1):
        if (personinfolist[item] == "Email:"):
            while(item < len(personinfolist)-1 and personinfolist[item+1] not in keywords):
                person.email += personinfolist[item+1]
                item += 1
        if (personinfolist[item] == "Title:"):
            while(item < len(personinfolist)-1 and personinfolist[item+1] not in keywords):
                person.title += personinfolist[item+1]
                item += 1
        if (personinfolist[item] == "Department:"):
            while(item < len(personinfolist)-1 and personinfolist[item+1] not in keywords):
                person.dept += personinfolist[item+1]
                item += 1
                person.dept += " "
        if (personinfolist[item] == "Phone:"):
            while(item < len(personinfolist)-1 and personinfolist[item+1] not in keywords):
                person.phone += personinfolist[item+1]
                item += 1
                person.phone += " "
        if (personinfolist[item] == "Address:"):
            while(item < len(personinfolist)-1 and personinfolist[item+1] not in keywords):
                person.address += personinfolist[item+1]
                item += 1
                person.address += " "
        if (personinfolist[item] == "City:"):
            while(item < len(personinfolist)-1 and personinfolist[item+1] not in keywords):
                person.city += personinfolist[item+1]
                item += 1
        if (personinfolist[item] == "State:"):
            while(item < len(personinfolist)-1 and personinfolist[item+1] not in keywords):
                person.state += personinfolist[item+1]
                item += 1
    return person


def getPerson(first, last):
    URL = f"https://missouri.edu/directory/people-results?firstName={first}&lastname={last}&department=&phoneno=&email=&Search=Find+Person"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    if(soup.find("p", {"class": "meta-result"}).text == "Your search returned too many results. Please provide more details."):
        return (Person.Person("Too many results", "", "", "", "", "", "", ""))
    elif(soup.find("h2", {"class": "miz-card__title miz-card__title--mark miz-card__title--news miz-graphik"}) is None):
        return (Person.Person("No results", "", "", "", "", "", "", ""))
    else:
        person = getPersonWithSoup(BeautifulSoup(page.content, "html.parser"))
        person = Person.rightstrip(person)
        return person