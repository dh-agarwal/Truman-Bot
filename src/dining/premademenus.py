import sys
sys.path.insert(1,'src/dining')
from timesdict import getTimesDict as getTimesDict

menuDict = {
    "1+5+3 Salads and Soups": ["https://dining.missouri.edu/locations/153-salads-and-soups/", "https://dining.missouri.edu/wp-content/uploads/sites/19/2019/05/153-logo-e1615579713594.jpg"],
    "1839 Kitchen": ["https://dining.missouri.edu/locations/1839-kitchen/", "https://dining.missouri.edu/wp-content/uploads/sites/19/2019/05/1839-768x668.jpg"],
    "Baja Grill": {
        "Entrees": ["Burrito", "Burrito Bowl", "Macho Nachos", "Nachos", "Quesadilla", "Quesadilla con Estilo", "Taco"],
        "Chips & Dips": ["Black Beans & Corn Salsa", "Chips & Guacamole", "Chips & Queso", "Chips & Salsa", "Grande Chips & Queso", "Grande Chips & Salsa", "Grande Queso Dip", "Guacamole", "Queso Dip", "Salsa Roja (Red Salsa)", "Signature Tortilla Chips"],
        "Extras": ["Pinto or Black Beans", "Red or Green Rice", "Sour Cream"],
        "Dessert": ["Bananas and Chocolate Quesadilla", "Double Chocolate Chip Cookies"],
        "Beverages": ["Soft Drink"],
        "Value Meals": ["Tres Quesadillas", "Tres Tacos"]
    },
    "Bookmark Café": ["https://dining.missouri.edu/locations/bookmark-cafe/", "https://dining.missouri.edu/wp-content/uploads/sites/19/2019/05/Bookmark_cafe-210x300.png"],
    "Catalyst Café": ["https://dining.missouri.edu/locations/catalyst-cafe/", "https://dining.missouri.edu/wp-content/uploads/sites/19/2019/05/Catalyst-768x324.png"],
    "Do Mundo's": ["https://dining.missouri.edu/locations/do-mundos/", "https://dining.missouri.edu/wp-content/uploads/sites/19/2019/05/DoMundos2-768x134.png"],
    "Emporium Café": ["https://dining.missouri.edu/locations/emporium-cafe/", "https://dining.missouri.edu/wp-content/uploads/sites/19/2019/05/Emporium_cafe-210x300.png"],
    "infusion": {
        "Customize: Hot Drink": ["Add a shot of espresso!", "Sub Soy Milk, Almond Milk, Half & Half, or Oat Milk", "Vanilla, Caramel, Sugar-free Vanilla and Chocolate"],
        "Hot Drinks": ["Americano", "Cappuccino", "Caramel Latte", "Chai Latte", "Chocolate Chai", "Coffee", "Double Shot of Espresso", "Hot Chocolate", "Hot Tea Packet", "Latte", "Matcha", "Mocha", "Vanilla Latte"]
    },
    "Legacy Grill": ["https://dining.missouri.edu/locations/legacy-grill/", "https://dining.missouri.edu/wp-content/uploads/sites/19/2019/05/LegacyGrill-300x194.png"],
    "Mort's": ["https://dining.missouri.edu/locations/morts/", "https://dining.missouri.edu/wp-content/uploads/sites/19/2019/05/Morts2.png"],
    "Olive & Oil": ["https://dining.missouri.edu/locations/olive-&-oil/", "https://dining.missouri.edu/wp-content/uploads/sites/19/2019/05/OliveandOil.png"],
    "Panda Express": ["https://dining.missouri.edu/locations/potential-energy-cafe/", "https://dining.missouri.edu/wp-content/uploads/sites/19/2019/05/Potentail-Energy-Logo.jpg"],
    "Plaza 900 Dining": 1,
    "Potential Energy Café": ["https://dining.missouri.edu/locations/sabai/", "https://dining.missouri.edu/wp-content/uploads/sites/19/2019/05/sabai.png"],
    "Pizza & MO": 1,
    "Breakfast & MO": 1,
    "Sabai": ["https://dining.missouri.edu/locations/sabai/", "https://dining.missouri.edu/wp-content/uploads/sites/19/2019/05/sabai.png"],
    "Starbucks": ["https://dining.missouri.edu/locations/starbucks-memorial-union/", "https://dining.missouri.edu/wp-content/uploads/sites/19/2019/05/starbucks.png"],
    "Subway": ["https://dining.missouri.edu/locations/subway-hitt-street/", "https://dining.missouri.edu/wp-content/uploads/sites/19/2019/05/subway.png"],
    "Sunshine Sushi": ["https://dining.missouri.edu/locations/sunshine-sushi/", "https://dining.missouri.edu/wp-content/uploads/sites/19/2019/05/sunshinesushi-300x150.png"],
    "The MARK on 5th Street": 1,
    "Tiger Avenue Deli": ["https://dining.missouri.edu/locations/tiger-avenue-deli/", "https://dining.missouri.edu/wp-content/uploads/sites/19/2019/05/Tiger-Avenue-Deli-Logo-e1615577624599.jpg"],
    "Truffles": ["https://dining.missouri.edu/locations/truffles/", "https://dining.missouri.edu/wp-content/uploads/sites/19/2019/05/Truffles-Logo.jpg"],
    "Wheatstone Bistro": ["https://dining.missouri.edu/locations/wheatstone-bistro/", "https://dining.missouri.edu/wp-content/uploads/sites/19/2019/05/WheatstoneBistro.png"]
}

infoDict = {
    "1+5+3 Salads and Soups": ["https://dining.missouri.edu/locations/153-salads-and-soups/", "https://dining.missouri.edu/wp-content/uploads/sites/19/2019/05/153-logo-e1615579713594.jpg"],
    "1839 Kitchen": ["https://dining.missouri.edu/locations/1839-kitchen/", "https://dining.missouri.edu/wp-content/uploads/sites/19/2019/05/1839-768x668.jpg"],
    "Baja Grill": ["https://dining.missouri.edu/locations/baja-grill/", "https://dining.missouri.edu/wp-content/uploads/sites/19/2019/05/BajaLogo-01.png"],
    "Bookmark Café": ["https://dining.missouri.edu/locations/bookmark-cafe/", "https://dining.missouri.edu/wp-content/uploads/sites/19/2019/05/Bookmark_cafe-210x300.png"],
    "Catalyst Café": ["https://dining.missouri.edu/locations/catalyst-cafe/", "https://dining.missouri.edu/wp-content/uploads/sites/19/2019/05/Catalyst-768x324.png"],
    "Do Mundo's": ["https://dining.missouri.edu/locations/do-mundos/", "https://dining.missouri.edu/wp-content/uploads/sites/19/2019/05/DoMundos2-768x134.png"],
    "Emporium Café": ["https://dining.missouri.edu/locations/emporium-cafe/", "https://dining.missouri.edu/wp-content/uploads/sites/19/2019/05/Emporium_cafe-210x300.png"],
    "infusion": ["https://dining.missouri.edu/locations/infusion/", "https://dining.missouri.edu/wp-content/uploads/sites/19/2019/05/Infusion-300x204.png"],
    "Legacy Grill": ["https://dining.missouri.edu/locations/legacy-grill/", "https://dining.missouri.edu/wp-content/uploads/sites/19/2019/05/LegacyGrill-300x194.png"],
    "Mort's": ["https://dining.missouri.edu/locations/morts/", "https://dining.missouri.edu/wp-content/uploads/sites/19/2019/05/Morts2.png"],
    "Olive & Oil": ["https://dining.missouri.edu/locations/olive-&-oil/", "https://dining.missouri.edu/wp-content/uploads/sites/19/2019/05/OliveandOil.png"],
    "Panda Express": ["https://dining.missouri.edu/locations/potential-energy-cafe/", "https://dining.missouri.edu/wp-content/uploads/sites/19/2019/05/Potentail-Energy-Logo.jpg"],
    "Plaza 900 Dining": ["https://dining.missouri.edu/locations/plaza-900-dining/", "https://dining.missouri.edu/wp-content/uploads/sites/19/2019/05/Plaza900.png"],
    "Potential Energy Café": ["https://dining.missouri.edu/locations/sabai/", "https://dining.missouri.edu/wp-content/uploads/sites/19/2019/05/sabai.png"],
    "Pizza & MO": [],
    "Breakfast & MO": [],
    "Sabai": ["https://dining.missouri.edu/locations/sabai/", "https://dining.missouri.edu/wp-content/uploads/sites/19/2019/05/sabai.png"],
    "Starbucks": ["https://dining.missouri.edu/locations/starbucks-memorial-union/", "https://dining.missouri.edu/wp-content/uploads/sites/19/2019/05/starbucks.png"],
    "Subway": ["https://dining.missouri.edu/locations/subway-hitt-street/", "https://dining.missouri.edu/wp-content/uploads/sites/19/2019/05/subway.png"],
    "Sunshine Sushi": ["https://dining.missouri.edu/locations/sunshine-sushi/", "https://dining.missouri.edu/wp-content/uploads/sites/19/2019/05/sunshinesushi-300x150.png"],
    "The MARK on 5th Street": ["https://dining.missouri.edu/locations/the-mark-on-5th-street/", "https://dining.missouri.edu/wp-content/uploads/sites/19/2019/05/themarkon5th-01.png"],
    "Tiger Avenue Deli": ["https://dining.missouri.edu/locations/tiger-avenue-deli/", "https://dining.missouri.edu/wp-content/uploads/sites/19/2019/05/Tiger-Avenue-Deli-Logo-e1615577624599.jpg"],
    "Truffles": ["https://dining.missouri.edu/locations/truffles/", "https://dining.missouri.edu/wp-content/uploads/sites/19/2019/05/Truffles-Logo.jpg"],
    "Wheatstone Bistro": ["https://dining.missouri.edu/locations/wheatstone-bistro/", "https://dining.missouri.edu/wp-content/uploads/sites/19/2019/05/WheatstoneBistro.png"]
}

class DiningHall:
    def __init__(self, name):
        self.name = name
        self.url = infoDict[name][0]
        self.logo = infoDict[name][1]
        self.menu = menuDict[name]
        self.times = getTimesDict(infoDict[name][0])