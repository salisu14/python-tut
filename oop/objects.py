#!/usr/bin/env python3

class Product:
    # a constructor that initializes 3 attributes
    def __init__(self, name, price, discountPercent):
        self.__name = name
        self.__price = price
        self.__discountPercent = discountPercent

    @property
    def name(self):
        return self.__name
    
    def getPrice(self):
        return self.__price
    
    def getDiscountPercent(self):
        return self.__discountPercent

    # a method that uses two attributes to perform calculation
    def getDiscountAmount(self):
        return self.__price * self.__discountPercent / 100
    
    # a method that calls another method to perform a calculation
    def getDiscountPrice(self):
        return self.__price - self.getDiscountAmount()
    

    