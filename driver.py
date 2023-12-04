from magclass import Pricelist
from magclass import TotalPrice

print("The food in stock are: \n 1. Dry Cured Iberian Ham \n 2. Wagyoo Steaks \n 3. Matsutake Mooshrooms \n 4. Luwak Coffee \n 5. Moose Cheese \n 6. White Truffles \n 7. Bluefin Tuna \n 8. Le Bonnotte Potatoos")

def CreateList():
    ItemNum = int(input("How many do you want to order? Input here: "))
    while ItemNum < 1 :
        print("uh, your order has to be more than zero? input again here: ")
     



    for i in range (ItemNum):
        itemList = []
        print("Item #", i)
        food = input("Enter Food:")
        amt = float(input("Enter pounds:"))
        
        while amt<0 :
            print("Oops, cannot.")

        MyFood = Pricelist
        itemList.append(MyFood)
        return itemList
    
def displayList(foodList):
    print("Here's the items purchased:")
    print("-----------------------------------------")

    for food in foodList:
        foodList[food].__str__()

def main():
    myFoodlist = CreateList()
    displayList(myFoodlist)        
