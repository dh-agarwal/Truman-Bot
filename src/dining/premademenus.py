import sys
sys.path.insert(1,'src/dining')
from timesdict import getTimesDict as getTimesDict

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

def getInfusionTimesDict():
    return getTimesDict("https://dining.missouri.edu/locations/infusion/")

def getInfusionMenu():
    return {
        "Customize: Hot Drink": ["Add a shot of espresso!", "Sub Soy Milk, Almond Milk, Half & Half, or Oat Milk", "Vanilla, Caramel, Sugar-free Vanilla and Chocolate"],
        "Hot Drinks": ["Americano", "Cappuccino", "Caramel Latte", "Chai Latte", "Chocolate Chai", "Coffee", "Double Shot of Espresso", "Hot Chocolate", "Hot Tea Packet", "Latte", "Matcha", "Mocha", "Vanilla Latte"]
    }

def getInfusionInfo():
    return ["https://dining.missouri.edu/locations/infusion/", "https://dining.missouri.edu/wp-content/uploads/sites/19/2019/05/Infusion-300x204.png"]