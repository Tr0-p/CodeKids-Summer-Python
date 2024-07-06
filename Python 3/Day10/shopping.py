# A class is a template, used to create objects


class Product:
    # constructor function
    # creates the object itself
    # "self" is only used within the class declaration
    def __init__(self, name, price):
        # saves the parameters
        # now they are called attributes (attributes of the class)
        self.name = name
        self.price = price

    def display_info(self):
        print(f"{self.name}: £{self.price}")


class Cart:
    def __init__(self):
        # a list of items inside our shopping cart
        self.items = []

    def addItem(self, item):
        self.items.append(item)
        print(f"You have added 1 {item.name}.")

    def previewCart(self):
        print("\n-----------")
        print("Your cart has:")
        total = 0

        for food in self.items:
            food.display_info()
            total = total + food.price

        print("-----------")
        print(f"Total: £{round(total, 2)}")


apple = Product("Apple", 0.5)
banana = Product("Banana", 0.25)
orange = Product("Orange", 0.6)

print(apple.price)

# apple.display_info()

shoppingCart = Cart()

shoppingCart.addItem(apple)
shoppingCart.addItem(banana)
shoppingCart.addItem(banana)
shoppingCart.addItem(orange)
shoppingCart.previewCart()


# ==========================


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} goes woof!")


# dog = Dog("The Dog", 2)
# dog.bark()
