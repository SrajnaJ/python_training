# Base class
class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def update_stock(self, quantity):
        if quantity < 0 and abs(quantity) > self.stock:
            print(f"Insufficient stock! Only {self.stock} left.")
        else:
            self.stock += quantity
            print(f"Stock updated! New stock: {self.stock}")

    def display_info(self):
        return f"Product: {self.name}, Price: ${self.price}, Stock: {self.stock}"

# Subclass for Electronics
class Electronics(Product):
    def __init__(self, name, price, stock, brand, warranty, specifications):
        super().__init__(name, price, stock)
        self.brand = brand
        self.warranty = warranty  # in years
        self.specifications = specifications  # dictionary of key-value specs

    def display_info(self):
        specs = ", ".join([f"{k}: {v}" for k, v in self.specifications.items()])
        return f"{super().display_info()}, Brand: {self.brand}, Warranty: {self.warranty} years, Specs: {specs}"

# Subclass for Clothing
class Clothing(Product):
    def __init__(self, name, price, stock, material, category, size):
        super().__init__(name, price, stock)
        self.material = material
        self.category = category  # e.g., "Men's Wear", "Women's Wear"
        self.size = size  # e.g., S, M, L, XL

    def display_info(self):
        return f"{super().display_info()}, Material: {self.material}, Category: {self.category}, Size: {self.size}"

# Example:-
laptop = Electronics("Laptop", 1000, 5, "Dell", 2, {"Processor": "Intel i7", "RAM": "16GB", "Storage": "512GB SSD"})
shirt = Clothing("T-Shirt", 20, 50, "Cotton", "Men's Wear", "L")

print(laptop.display_info())
print(shirt.display_info())

laptop.update_stock(-1)
shirt.update_stock(10)
