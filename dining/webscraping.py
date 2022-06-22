from bs4 import BeautifulSoup
from datetime import date
import calendar
import requests

URL = "https://musis1.missouri.edu/gradedist/mu_grade_dist_intro.cfm#CGI.script.name#"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

mydivs = soup.find_all("tr")
print(mydivs)
# for i in mydivs:
#     print(i)
#     print("\n")