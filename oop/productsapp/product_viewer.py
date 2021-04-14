from objects import Product, Book, Movie

def show_products(products):
    print("PRODUCTS")
    for i in range(len(products)):
        product = products[i]
        print(str(i+1) + ". " + product.getDescription())
    print()

def show_product(product):
    print("PRODUCT DATA")
    print("Name:           ", product.name)
    if isinstance(product, Book):
        print("Author:         ", product.author)
    if isinstance(product, Movie):
        print("Year:           ", product.year)
    print(f"Discount price:  {product.getDiscountPrice():.2f}")
    print()

def main():
    print("The Product Viewer program")
    print()

    products = (Product("Stanley 13 Ounce wood Hammer", 12.99, 62),
                Product('National Hardware 3/4" Wire Nails', 5.06, 5),
                Book("The Big Short", 15.95, 34, "Michael Lewis"),
                Movie("The Holy Grail - DVD", 14.99, 68, 1975))
    show_products(products)

    while True:
        number = int(input("Enter product number: "))
        print()

        product = products[number - 1]
        show_product(product)

        choice = input("Continue? (y/n): ").lower()
        print()
        if choice != "y":
            break

if __name__ == '__main__':
    main()