class ProductsStock:
    def __init__(self, name:str, price: float, quantity: int):
        self._name = name
        self._price = price
        self._quantity = quantity

    def total_value_in_stock(self):
        return self._price*self._quantity

    def add_products(self, quantity:int):
        self._quantity += quantity

    def remove_products(self, quantity:int):
        self._quantity -= quantity

    def __str__(self):
        return f"{self._name.upper()}, $ {self._price:.2f}, {self._quantity} units, Total: $ {self.total_value_in_stock():.2f}"

name_product = input("Name Product: ")
price_product = float(input("Price Product: "))
quantity_product = int(input("Quantity Product: "))
product = ProductsStock(name_product, price_product, quantity_product)

print("\n", product, "\n")

quantity = int(input("How many products do you wanna add in stock? "))
product.add_products(quantity)
print("\n", product, "\n")

quantity = int(input("How many products do you wanna remove from stock? "))
product.remove_products(quantity)
print("\n", product, "\n")