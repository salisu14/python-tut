#!/usr/bin/env python3

class Product:
    # a constructor that initializes 3 attributes
    def __init__(self, name="", price=0.0, discountPercent=0):
        self.__name = name
        self.__price = price
        self.__discountPercent = discountPercent

    @property
    def name(self):
        return self.__name
    
    @property
    def price(self):
        return self.__price
    
    @property
    def discountPercent(self):
        return self.__discountPercent

    # a method that uses two attributes to perform calculation
    def getDiscountAmount(self):
        return self.__price * self.__discountPercent / 100
    
    # a method that calls another method to perform a calculation
    def getDiscountPrice(self):
        return self.__price - self.getDiscountAmount()

    # a method to display the description of a product
    def getDescription(self):
        return self.name
    
    def __str__(self):
        return self.getDescription() + "|" + str(self.price) + "|" + str(self.discountPercent)

class Book(Product):
    def __init__(self, name="", price=0.0, discountPercent=0, author=""):
        Product.__init__(self, name, price, discountPercent)
        self.author = author
    
    def getDescription(self):
        return Product.getDescription(self) + " by " + self.author

class Movie(Product):
    def __init__(self, name="", price=0.0, discountPercent=0, year=0):
        Product.__init__(self, name, price, discountPercent)
        self.year = year
    
    def getDescription(self):
        return Product.getDescription(self) + " (" + str(self.year) + ")"

    