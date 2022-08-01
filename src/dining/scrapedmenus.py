#Plaza900
#PizzaAndMO?
#BreakfastAndMO?
from bs4 import BeautifulSoup
import requests

URL = "https://dining.missouri.edu/locations/bookmark-cafe/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
text = soup.find_all("td")
i = 0
newlist = []
for item in text:
    if (i%2 == 0):
        newlist.append((item.text).replace("\n", "").replace("\t", ""))
    i += 1

#print(newlist[:-7])
alltext = soup.text.replace("\n", "").replace("\t", "")
fooddict = {}
headers = soup.find_all("button", class_="miz-button miz-button--primary miz-button--light accordion__button")
# for food in range(len(newlist)):
#     for char in range(len(newlist[food])-1):
#         if newlist[food][char].islower() and newlist[food][char+1] != ' ' and newlist[food][char+1].isupper():
#             newlist[food] = (newlist[food][:char+1]) + '\n' + newlist[food][char+1:]
# print(headers)
#print(len(headers))
for header in range(len(headers)):
    txt1 = headers[header].text.replace("\n", "").replace("\t", "").replace("add", "").replace("search", "").replace("menu", "").replace("Dining Plansarrow_drop_down", "")
    # print(txt1)
    #print(header)
    if header != len(headers)-1:
        txt2 = headers[header+1].text.replace("\n", "").replace("\t", "").replace("add", "").replace("search", "").replace("menu", "").replace("Dining Plansarrow_drop_down", "")
        #print("in")
    foodlist = []
    # print(txt1)
    # print('\n\n')
    # print(alltext[alltext.find(txt1)-2:alltext.find(txt2)+3])
    # print('\n\n\n')
    if header != len(headers)-1:
        for food in newlist:
            if food in alltext[alltext.find(txt1)-2:alltext.find(txt2)+3]:
                for char in range(len(food)-1):
                    if food[char].islower() and food[char+1] != ' ' and food[char+1].isupper():
                        food = (food[:char+1]) + ':\n- ' + food[char+1:]
                foodlist.append(food)
                fooddict[txt1] = foodlist
    else:
        for food in newlist:
            if food in alltext[alltext.find(txt1)-2:]:
                for char in range(len(food)-1):
                    if food[char].islower() and food[char+1] != ' ' and food[char+1].isupper():
                        food = (food[:char+1]) + ':\n- ' + food[char+1:]
                foodlist.append(food)
                fooddict[txt1] = foodlist
    {'Coffee, Tea & Espresso': ['Café Americano', 'Café Caramel', 'Café Latte', 'Café Mocha', 'Cappuccino', 'Caramel Macchiato', 'Chai Tea Latte', 'Coffee', 'Cold Brew Iced Coffee', 'Green Tea Latte', 'Honey Almond Cold Brew', 'Hot Chocolate', 'Hot Tea', 'Spiced Hot Chocolate', 'Spiced Mocha', 'Strawberry Acai Refresher', 'Tiger Eye', 'Turtle Latte', 'Vanilla Latte', 'White Mocha'], 'Fraps & Smoothies': ['Frappe:\n- Mocha, Caramel, Java Chip, Green Tea, Turtle', 'Frappe:\n- Cookies and Cream', 'Smoothies:\n- Strawberry Banana, Pineapple Paradise, Peach Pear Apricot'], 'Pastries': ['Bagels:\n- Everything, Blueberry, Plain', 'Cookies:\n- Chocolate Chip', 'Cream Cheese:\n- Plain, Strawberry', 'Gluten Free Bagels:\n- Plain', 'Gluten Free Muffins:\n- Blueberry, Double Chocolate', "Lenny & Larry's Complete Cookies (vegan)Double Chocolate, Snickerdoodle ", 'Muffins:\n- Blueberry, Double Chocolate, Lemon Cranberry'], 'Bottled Beverages': ['Apple Juice', 'Bottled Soda, Chocolate Milk, Life Water, Gatorade, Propel', 'Bubly', 'Monster', 'Orange Juice'], 'Snacks': ['Chips:\n- Assorted Kettle Chips, Hot Cheetos, Harvest Cheddar Sun Chips', 'CLIF Bar:\n- Chocolate Chip, Peanut Butter ', 'Fruit Cup', 'Rice Marshmallow Treat (Gluten Free)', 'Sabra Avocado Spread with Toast Chips', 'Sabra Roasted Red Pepper Hummus with Pretzels', 'String Cheese', 'Trail Mix'], 'Available While Supplies Last': ["Ellianna's Donuts:\n- Glazed, Chocolate Cake, Blueberry Cake, Vanilla Cake", "Ellianna's Donuts:\n- Classic Donut with Icing and/or Sprinkles", "Ellianna's Donuts:\n- Bear Claw, Twist, Long John, Bismark", 'Taylor Farms Salads:\n- BLT, Fiesta', 'Taylor Farms Sandwiches:\n- Ham & Cheese on Pretzel, Turkey and Cheese Pinwheel, Chicken Caesar Wrap', 'Today 7/31/2022', 'Monday 8/1/2022', 'Tuesday 8/2/2022', 'Wednesday 8/3/2022', 'Thursday 8/4/2022', 'Friday 8/5/2022', 'Saturday 8/6/2022']}
{'Coffee, Tea & Espresso': ['Café Americano', 'Café Caramel', 'Café Latte', 'Café Mocha', 'Cappuccino', 'Caramel Macchiato', 'Chai Tea Latte', 'Coffee', 'Cold Brew Iced Coffee', 'Green Tea Latte', 'Honey Almond Cold Brew', 'Hot Chocolate', 'Hot Tea', 'Spiced Hot Chocolate', 'Spiced Mocha', 'Strawberry Acai Refresher', 'Tiger Eye', 'Turtle Latte', 'Vanilla Latte', 'White Mocha'], 'Fraps & Smoothies': ['Frappe\n-- Mocha, Caramel, Java Chip, Green Tea, Turtle', 'Frappe\n-- Cookies and Cream', 'Smoothies\n-- Strawberry Banana, Pineapple Paradise, Peach Pear Apricot'], 'Pastries': ['Bagels\n-- Everything, Blueberry, Plain', 'Cookies\n-- Chocolate Chip', 'Cream Cheese\n-- Plain, Strawberry', 'Gluten Free Bagels\n-- Plain', 'Gluten Free Muffins\n-- Blueberry, Double Chocolate', "Lenny & Larry's Complete Cookies (vegan)Double Chocolate, Snickerdoodle ", 'Muffins\n-- Blueberry, Double Chocolate, Lemon Cranberry'], 'Bottled Beverages': ['Apple Juice', 'Bottled Soda, Chocolate Milk, Life Water, Gatorade, Propel', 'Bubly', 'Monster', 'Orange Juice'], 'Snacks': ['Chips\n-- Assorted Kettle Chips, Hot Cheetos, Harvest Cheddar Sun Chips', 'CLIF Bar\n-- Chocolate Chip, Peanut Butter ', 'Fruit Cup', 'Rice Marshmallow Treat (Gluten Free)', 'Sabra Avocado Spread with Toast Chips', 'Sabra Roasted Red Pepper Hummus with Pretzels', 'String Cheese', 'Trail Mix'], 'Available While Supplies Last': ["Ellianna's Donuts\n-- Glazed, Chocolate Cake, Blueberry Cake, Vanilla Cake", "Ellianna's Donuts\n-- Classic Donut with Icing and/or Sprinkles", "Ellianna's Donuts\n-- Bear Claw, Twist, Long John, Bismark", 'Taylor Farms Salads\n-- BLT, Fiesta', 'Taylor Farms Sandwiches\n-- Ham & Cheese on Pretzel, Turkey and Cheese Pinwheel, Chicken Caesar Wrap', 'Today 7/31/2022', 'Monday 8/1/2022', 'Tuesday 8/2/2022', 'Wednesday 8/3/2022', 'Thursday 8/4/2022', 'Friday 8/5/2022', 'Saturday 8/6/2022']}        
    #print(f"\"{txt}\": [],")
# print("\n\n")

# print(alltext)
# print('\n\n')
# print(alltext.find('Bagels and Cream Cheese'))
# fooddict.pop('')
# fooddict.pop('    ')
print(fooddict)
# print('\n\n\n')
# print(alltext)
# print('\n\n\n')
# print(newlist)
