#!/usr/bin/env python3
from objects import Product


#  a function to display objects data
def print_data(obj):
    # print data for the given object to console
    print(f"Name:             {obj.name:s}")
    print(f"Price:            {obj.getPrice():.2f}")
    print(f"Discount percent: {obj.getDiscountPercent():d}%")
    print(f"Discount amount:  {obj.getDiscountAmount():.2f}")
    print(f"Discount price:   {obj.getDiscountPrice():.2f}")
    print("-------------------------------------------------------")
    print()

def main():
    # create two product objects
    product1 = Product("Stanley 13 Ounce wood Hammer", 12.99, 62)
    product2 = Product('National Hardware 3/4" Wire Nails', 5.06, 5)

    # print data for product1 to console
    print_data(product1)

    # print data for product2 to console
    print_data(product2)
    


if __name__ == '__main__':
    main()