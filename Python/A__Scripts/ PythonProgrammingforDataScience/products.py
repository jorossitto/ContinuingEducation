# objects.py

class Product:
    def __init__(self, name="", price=0.0, discountPercent=0):
        self.name = name
        self.price = price
        self.discountPercent = discountPercent

    def getDiscountAmount(self):
        return self.price * self.discountPercent / 100

    def getDiscountPrice(self):
        return self.price - self.getDiscountAmount()

    def getDescription(self):
        return self.name


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

class Car(Product):
    def __init__(self, name="", price=0.0, discountPercent=0, year=0, model = ""):
        Product.__init__(self, name, price, discountPercent)
        self.year = year
        self.model = model

    def getDescription(self):
        return Product.getDescription(self) \
               + " (" + str(self.year) + ")" \
               + " (" + str(self.model) + ")"

# product_viewer.py

#from objects import Product, Book, Movie


def show_products(products):
    print("PRODUCTS")
    for i in range(len(products)):
        product = products[i]
        print(str(i + 1) + ".", product.getDescription())
    print()


def show_product(product):
    print("PRODUCT DATA")
    print("Name:            ", product.name)
    if isinstance(product, Book):
        print("Author:          ", product.author)
    if isinstance(product, Movie):
        print("Year:            ", product.year)
    if isinstance(product, Car):
        print("Year:            ", product.year)
        print("Model:            ", product.model)
    print("Discount price:   {:.2f}".format(product.getDiscountPrice()))
    print()


def main():
    print("The Product Viewer program")
    print()

    # a tuple of Product objects
    products = (Product('Stanley 13 Ounce Wood Hammer', 12.99, 62),
                Book("The Big Short", 15.95, 34, "Michael Lewis"),
                Movie("The Holy Grail - DVD", 14.99, 68, 1975),
                Car("Toyota", 19999, 10, 2015, "Prius"))

    show_products(products)

    while True:
        number = int(input("Enter product number: "))
        print()

        product = products[number - 1]
        show_product(product)

        choice = input("Continue? (y/n): ")
        print()
        if choice != "y":
            print("Bye!")
            break


if __name__ == "__main__":
    main()