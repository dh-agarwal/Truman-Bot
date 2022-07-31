from re import M
import sys
sys.path.insert(1,'src/dining')
from timesdict import getTimesDict as getTimesDict

menuDict = {
    "Baja Grill": {
        "Entrees": ["Burrito", "Burrito Bowl", "Macho Nachos", "Nachos", "Quesadilla", "Quesadilla con Estilo", "Taco"],
        "Chips & Dips": ["Black Beans & Corn Salsa", "Chips & Guacamole", "Chips & Queso", "Chips & Salsa", "Grande Chips & Queso", "Grande Chips & Salsa", "Grande Queso Dip", "Guacamole", "Queso Dip", "Salsa Roja (Red Salsa)", "Signature Tortilla Chips"],
        "Extras": ["Pinto or Black Beans", "Red or Green Rice", "Sour Cream"],
        "Dessert": ["Bananas and Chocolate Quesadilla", "Double Chocolate Chip Cookies"],
        "Beverages": ["Soft Drink"],
        "Value Meals": ["Tres Quesadillas", "Tres Tacos"]
    },
    "infusion": {
        "Customize: Hot Drink": ["Add a shot of espresso!", "Sub Soy Milk, Almond Milk, Half & Half, or Oat Milk", "Vanilla, Caramel, Sugar-free Vanilla and Chocolate"],
        "Hot Drinks": ["Americano", "Cappuccino", "Caramel Latte", "Chai Latte", "Chocolate Chai", "Coffee", "Double Shot of Espresso", "Hot Chocolate", "Hot Tea Packet", "Latte", "Matcha", "Mocha", "Vanilla Latte"]
    }
}

infoDict = {
    "1+5+3 Salads and Soups":,
    "1839 Kitchen":,
    "Baja Grill": ["https://dining.missouri.edu/locations/baja-grill/", "https://dining.missouri.edu/wp-content/uploads/sites/19/2019/05/BajaLogo-01.png"],
    "Bookmark Café":,
    "Catalyst Café":,
    "Do Mundo's":,
    "Emporium Café":,
    "infusion": ["https://dining.missouri.edu/locations/infusion/", "https://dining.missouri.edu/wp-content/uploads/sites/19/2019/05/Infusion-300x204.png"],
    "Legacy Grill":,
    "Mort's":,
    "Olive & Oil":,
    "Panda Express":,
    "Plaza 900 Dining",
    "Potential Energy Café"
    "Pizza & MO"
    "Breakfast & MO"
    "Sabai"
    "Starbucks"
    "Subway"
    "Sunshine Sushi"
    "The MARK on 5th Street"
    "Tiger Avenue Deli"
    "Truffles"
    "Wheatstone Bistro"

}

class DiningHall:
    def __init__(self, name):
        self.name = name
        self.url = infoDict[name][0]
        self.logo = infoDict[name][1]
        self.menu = menuDict[name]
        self.times = getTimesDict(infoDict[name][0])

#153SaladSoups
def get153SaladSoupsTimesDict():
    return getTimesDict("https://dining.missouri.edu/locations/153-salads-and-soups/")

def get153SaladSoupsMenu():
    return {

    }

def get153SaladSoupsInfo():
    return ["https://dining.missouri.edu/locations/153-salads-and-soups/", "https://dining.missouri.edu/wp-content/uploads/sites/19/2019/05/153-logo-e1615579713594.jpg"]


#1839Kitchen
def get1839KitchenTimesDict():
    return getTimesDict("https://dining.missouri.edu/locations/1839-kitchen/")

def get1839KitchenMenu():
    return {

    }

def get1839KitchenInfo():
    return ["https://dining.missouri.edu/locations/1839-kitchen/", "https://dining.missouri.edu/wp-content/uploads/sites/19/2019/05/1839-768x668.jpg"]


#Baja
def getBajaTimesDict():
    return getTimesDict("https://dining.missouri.edu/locations/baja-grill/")

def getBajaMenu():
    return {
        "Entrees": ["Burrito", "Burrito Bowl", "Macho Nachos", "Nachos", "Quesadilla", "Quesadilla con Estilo", "Taco"],
        "Chips & Dips": ["Black Beans & Corn Salsa", "Chips & Guacamole", "Chips & Queso", "Chips & Salsa", "Grande Chips & Queso", "Grande Chips & Salsa", "Grande Queso Dip", "Guacamole", "Queso Dip", "Salsa Roja (Red Salsa)", "Signature Tortilla Chips"],
        "Extras": ["Pinto or Black Beans", "Red or Green Rice", "Sour Cream"],
        "Dessert": ["Bananas and Chocolate Quesadilla", "Double Chocolate Chip Cookies"],
        "Beverages": ["Soft Drink"],
        "Value Meals": ["Tres Quesadillas", "Tres Tacos"]
    }

def getBajaInfo():
    return ["https://dining.missouri.edu/locations/baja-grill/", "https://dining.missouri.edu/wp-content/uploads/sites/19/2019/05/BajaLogo-01.png"]


#BookmarkCafe
def getBookmarkCafeTimesDict():
    return getTimesDict("https://dining.missouri.edu/locations/bookmark-cafe/")

def getBookmarkCafeMenu():
    return {

    }

def getBookmarkCafeInfo():
    return ["https://dining.missouri.edu/locations/bookmark-cafe/", "https://dining.missouri.edu/wp-content/uploads/sites/19/2019/05/Bookmark_cafe-210x300.png"]


#CatalystCafe
def getCatalystCafeTimesDict():
    return getTimesDict("https://dining.missouri.edu/locations/catalyst-cafe/")

def getCatalystCafeMenu():
    return {

    }

def getCatalystCafeInfo():
    return ["https://dining.missouri.edu/locations/catalyst-cafe/", "https://dining.missouri.edu/wp-content/uploads/sites/19/2019/05/Catalyst-768x324.png"]


#DoMundos
def getDoMundosTimesDict():
    return getTimesDict("https://dining.missouri.edu/locations/do-mundos/")

def getDoMundosMenu():
    return {

    }

def getDoMundosInfo():
    return ["https://dining.missouri.edu/locations/do-mundos/", "https://dining.missouri.edu/wp-content/uploads/sites/19/2019/05/DoMundos2-768x134.png"]


#Emporium
def getEmporiumTimesDict():
    return getTimesDict("https://dining.missouri.edu/locations/emporium-cafe/")

def getEmporiumMenu():
    return {

    }

def getEmporiumInfo():
    return ["https://dining.missouri.edu/locations/emporium-cafe/", "https://dining.missouri.edu/wp-content/uploads/sites/19/2019/05/Emporium_cafe-210x300.png"]


#Infusion
def getInfusionTimesDict():
    return getTimesDict("https://dining.missouri.edu/locations/infusion/")

def getInfusionMenu():
    return {
        "Customize: Hot Drink": ["Add a shot of espresso!", "Sub Soy Milk, Almond Milk, Half & Half, or Oat Milk", "Vanilla, Caramel, Sugar-free Vanilla and Chocolate"],
        "Hot Drinks": ["Americano", "Cappuccino", "Caramel Latte", "Chai Latte", "Chocolate Chai", "Coffee", "Double Shot of Espresso", "Hot Chocolate", "Hot Tea Packet", "Latte", "Matcha", "Mocha", "Vanilla Latte"]
    }

def getInfusionInfo():
    return ["https://dining.missouri.edu/locations/infusion/", "https://dining.missouri.edu/wp-content/uploads/sites/19/2019/05/Infusion-300x204.png"]


#LegacyGrill
def getLegacyGrillTimesDict():
    return getTimesDict("https://dining.missouri.edu/locations/legacy-grill/")

def getLegacyGrillMenu():
    return {

    }

def getLegacyGrillInfo():
    return ["https://dining.missouri.edu/locations/legacy-grill/", "https://dining.missouri.edu/wp-content/uploads/sites/19/2019/05/LegacyGrill-300x194.png"]


#Morts
def getMortsTimesDict():
    return getTimesDict("https://dining.missouri.edu/locations/morts/")

def getMortsMenu():
    return {

    }

def getMortsInfo():
    return ["https://dining.missouri.edu/locations/morts/", "https://dining.missouri.edu/wp-content/uploads/sites/19/2019/05/Morts2.png"]


#OliveAndOil
def getOliveAndOilTimesDict():
    return getTimesDict("https://dining.missouri.edu/locations/olive-&-oil/")

def getOliveAndOilMenu():
    return {

    }

def getOliveAndOilInfo():
    return ["https://dining.missouri.edu/locations/olive-&-oil/", "https://dining.missouri.edu/wp-content/uploads/sites/19/2019/05/OliveandOil.png"]


#OliveAndOil
def getOliveAndOilTimesDict():
    return getTimesDict("https://dining.missouri.edu/locations/olive-&-oil/")

def getOliveAndOilMenu():
    return {

    }

def getOliveAndOilInfo():
    return ["https://dining.missouri.edu/locations/olive-&-oil/", "https://dining.missouri.edu/wp-content/uploads/sites/19/2019/05/OliveandOil.png"]


#PotentialEnergyCafe
def getPotentialEnergyCafeTimesDict():
    return getTimesDict("https://dining.missouri.edu/locations/potential-energy-cafe/")

def getPotentialEnergyCafeMenu():
    return {

    }

def getPotentialEnergyCafeInfo():
    return ["https://dining.missouri.edu/locations/potential-energy-cafe/", "https://dining.missouri.edu/wp-content/uploads/sites/19/2019/05/Potentail-Energy-Logo.jpg"]


#PotentialEnergyCafe
def getPotentialEnergyCafeTimesDict():
    return getTimesDict("https://dining.missouri.edu/locations/sabai/")

def getPotentialEnergyCafeMenu():
    return {

    }

def getPotentialEnergyCafeInfo():
    return ["https://dining.missouri.edu/locations/sabai/", "https://dining.missouri.edu/wp-content/uploads/sites/19/2019/05/sabai.png"]
    