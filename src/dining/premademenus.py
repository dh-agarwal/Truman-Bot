import sys
sys.path.insert(1,'src/dining')
from timesdict import getTimesDict as getTimesDict
import datetime

soupsdict = {
    0: "Broccoli Cheese",
    1: "Cream of Tomato Soup",
    2: "White Chicken Chili",
    3: "Shrimp and wild Rice Soup",
    4: "Potato Soup",
    5: "None",
    6: "None"
}

menuDict = {
    "1+5+3 Salads and Soups": {
        "Salads": ["1+5+3 Salad", "Avocado Toast", "Extras", "Southwestern Salad"],
        "Beverages": ["Fountain Soda"],
        "Soups": ['Broccoli Cheese Monday ONLY', 'Cream of Tomato Soup Tuesday ONLY', 'Potato SoupFriday ONLY', 'Shrimp and wild Rice Soup Thursday ONLY', 'White Chicken Chili Wednesday ONLY']
    },
    "1839 Kitchen": {
        "Breakfast": ["1839 Platter, Choice of eggs or meat", "Bacon", "Biscuit", "Chicken and Apple Sausage", "Cinnamon roll", "Hard Cooked Eggs", "Peppered Gravy", "Sausage Patties", "Scrambled Eggs", "Steel Cut Oats", "Tater Tots"],
        "Lunch and Dinner": ["Daily Protein", "Rotisserie Chicken"],
        "Sides": ["Apple cheese cup", "Baked Potato", "Blueberry Parfait", "Chocolate partfait", "Country Style Green Beans", "Cut fruit", "Mashed Potatoes/Gravy", "Roll", "Veg du Jour"],
        "Beverages": ["2% Milk", "Almond Chocoalte milk", "Apple juice", "Bottled Water", "Chocolate milk", "Cran-Grape juice", "fountain drink", "Orange juice", "Soy Silk Chocolate milk"]
    },
    "Baja Grill": {
        "Entrees": ["Burrito", "Burrito Bowl", "Macho Nachos", "Nachos", "Quesadilla", "Quesadilla con Estilo", "Taco"],
        "Chips & Dips": ["Black Beans & Corn Salsa", "Chips & Guacamole", "Chips & Queso", "Chips & Salsa", "Grande Chips & Queso", "Grande Chips & Salsa", "Grande Queso Dip", "Guacamole", "Queso Dip", "Salsa Roja (Red Salsa)", "Signature Tortilla Chips"],
        "Extras": ["Pinto or Black Beans", "Red or Green Rice", "Sour Cream"],
        "Dessert": ["Bananas and Chocolate Quesadilla", "Double Chocolate Chip Cookies"],
        "Beverages": ["Soft Drink"],
        "Value Meals": ["Tres Quesadillas", "Tres Tacos"]
    },
    "Bookmark Café":     {'Coffee, Tea & Espresso': ['Café Americano', 'Café Caramel', 'Café Latte', 'Café Mocha', 'Cappuccino', 'Caramel Macchiato', 'Chai Tea Latte', 'Coffee', 'Cold Brew Iced Coffee', 'Green Tea Latte', 'Honey Almond Cold Brew', 'Hot Chocolate', 'Hot Tea', 'Spiced Hot Chocolate', 'Spiced Mocha', 'Strawberry Acai Refresher', 'Tiger Eye', 'Turtle Latte', 'Vanilla Latte', 'White Mocha'], 'Fraps & Smoothies': ['Frappe:\n- Mocha, Caramel, Java Chip, Green Tea, Turtle', 'Frappe:\n- Cookies and Cream', 'Smoothies:\n- Strawberry Banana, Pineapple Paradise, Peach Pear Apricot'], 'Pastries': ['Bagels:\n- Everything, Blueberry, Plain', 'Cookies:\n- Chocolate Chip', 'Cream Cheese:\n- Plain, Strawberry', 'Gluten Free Bagels:\n- Plain', 'Gluten Free Muffins:\n- Blueberry, Double Chocolate', "Lenny & Larry's Complete Cookies (vegan)Double Chocolate, Snickerdoodle ", 'Muffins:\n- Blueberry, Double Chocolate, Lemon Cranberry'], 'Bottled Beverages': ['Apple Juice', 'Bottled Soda, Chocolate Milk, Life Water, Gatorade, Propel', 'Bubly', 'Monster', 'Orange Juice'], 'Snacks': ['Chips:\n- Assorted Kettle Chips, Hot Cheetos, Harvest Cheddar Sun Chips', 'CLIF Bar:\n- Chocolate Chip, Peanut Butter ', 'Fruit Cup', 'Rice Marshmallow Treat (Gluten Free)', 'Sabra Avocado Spread with Toast Chips', 'Sabra Roasted Red Pepper Hummus with Pretzels', 'String Cheese', 'Trail Mix'], 'Available While Supplies Last': ["Ellianna's Donuts:\n- Glazed, Chocolate Cake, Blueberry Cake, Vanilla Cake", "Ellianna's Donuts:\n- Classic Donut with Icing and/or Sprinkles", "Ellianna's Donuts:\n- Bear Claw, Twist, Long John, Bismark", 'Taylor Farms Salads:\n- BLT, Fiesta', 'Taylor Farms Sandwiches:\n- Ham & Cheese on Pretzel, Turkey and Cheese Pinwheel, Chicken Caesar Wrap', 'Today 7/31/2022', 'Monday 8/1/2022', 'Tuesday 8/2/2022', 'Wednesday 8/3/2022', 'Thursday 8/4/2022', 'Friday 8/5/2022', 'Saturday 8/6/2022']}

,
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