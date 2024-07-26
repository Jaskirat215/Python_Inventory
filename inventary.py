from dicount import Sales 
class Item:
    def __init__(self, item_id, brand, model, price):
        self.item_id = item_id
        self.brand = brand
        self.model = model
        self.price = price

    def display_info(self):
        print("---------------------Details--------------------------")
        print(f"ID: {self.item_id}")
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Price: ${self.price}")

class Phone(Item):
    def __init__(self, item_id, brand, model, price, storage, camera_megapixels):
        super().__init__(item_id, brand, model, price)
        self.storage = storage
        self.camera_megapixels = camera_megapixels

    def display_info(self):
        super().display_info()
        print(f"Storage: {self.storage}GB")
        print(f"Camera: {self.camera_megapixels}MP")

class Laptop(Item):
    def __init__(self, item_id, brand, model, price, ram, processor):
        super().__init__(item_id, brand, model, price)
        self.ram = ram
        self.processor = processor

    def display_info(self):
        super().display_info()
        print(f"RAM: {self.ram}GB")
        print(f"Processor: {self.processor}")
phone1 = Phone(item_id=1, brand="Apple", model="iPhone 13", price=999, storage=128, camera_megapixels=12)
laptop1 = Laptop(item_id=2, brand="Dell", model="XPS 13", price=1299, ram=16, processor="Intel i7")
phone1.display_info()
phonediscounted = Sales.applydiscount(phone1.price, 10)  
phonesales = Sales.calculatesalesprice(phonediscounted, 8)
print(f"Sales Price : ${phonesales}") 
print(f"Discounted Price: ${phonediscounted}")
print("-------------------------------------------------------")
laptop1.display_info()
laptopdiscounted = Sales.applydiscount(laptop1.price, 15)  
laptopsales = Sales.calculatesalesprice(laptopdiscounted, 8) 
print(f"Sales Price after Tax: ${laptopsales}")
print(f"Discounted Price: ${laptopdiscounted}")
print("-------------------------------------------------------")

