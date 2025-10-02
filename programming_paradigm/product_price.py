class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

        
    def product_total(self):
        print(f"Name of product: {self.name}")
        print(f"Quantity of product: {self.quantity}")
        total = self.price * self.quantity
        print(f"Total: ${total}")
        


product = Product("Laptop", 1000, 3)
product.product_total()