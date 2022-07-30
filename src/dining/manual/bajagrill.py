from bs4 import BeautifulSoup
import requests
import sys
sys.path.insert(1,'src/dining')
from timesdict import getTimesDict as getTimesDict

URL = "https://dining.missouri.edu/locations/baja-grill/"

timesDict = getTimesDict(URL)

def getBajaTimesDict():
    return timesDict

def getBajaMenu():
    return {
        "Entrees": ["Burrito", "Burrito Bowl", "Macho Nachos", "Nachos", "Quesadilla", "Quesadilla con Estilo", "Taco"],
        "Chips & Dips": ["Black Beans & Corn Salsa", "Chips & Guacamole", "Chips & Queso", "Chips & Salsa", "Grande Chips & Queso", "Grande Chips & Salsa", "Grande Queso Dip", "Guacamole", "Queso Dip", "Salsa Roja (Red Salsa)", "Signature Tortilla Chips"],
        "Extras": ["Pinto or Black Beans", "Red or Green Rice", "Sour Cream"],
        "Dessert": ["Bananas and Chocolate Quesadilla", "Double Chocolate Chip Cookies"],
        "Beverages": ["Soft Drink"],
        "Value Meals": ["Tres Quesadillas", "Tres Tacos"]
    }