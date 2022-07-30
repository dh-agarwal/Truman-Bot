from bs4 import BeautifulSoup
import requests
import sys
sys.path.insert(1,'src/dining')
from manual.bajagrill import getBajaMenu as getBajaMenu
from manual.bajagrill import getBajaTimesDict as getBajaTimesDict