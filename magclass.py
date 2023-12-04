class Pricelist():
    __totalCost: 0.0
    def __init__(self, name, amount):
        self.__name = name
        self.__amount = amount
        self.__price = 0
        self.__total = 0
def PriceList(self):
    foodname = self.__name
    if foodname == 'Dry Cured Iberian Ham':
        self.__price = 177.80
        return self.__price
    elif foodname == 'Wagyu Steaks':
        self.__price = 450.00
        return self.__price
    elif foodname == 'Matsutake Mooshrooms':
        self.__price = 272.00
        return self.__price
    elif foodname == 'Moose Cheese':
        self.__price = 487.20
        return self.__price
    elif foodname == 'White Truffles': 
        self.__price = 3600.00
        return self.__price
    elif foodname == 'Bluefin Tuna':
        self.__price = 3603.00
        return self.__price
    elif foodname == 'Le Bonnotte Potatoos':
        self.__price = 270.81
        return self.__price
    else:
        print('Invalid Food Name')
class TotalPrice():
    def __init__(self, price):
        self.__price = price
    def total_cost(self):
        self.__total = self.__price * self.__amount 
        return self.__total
        
def __str__(self):
    return f"the total cost for {self.__amount} pounds of {self.__name} is {self.__total}"