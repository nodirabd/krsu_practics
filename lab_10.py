class Commodity:
    category = "General Goods"

    def __init__(self, id, productCode, name, wholesalePrice, retailPrice, description):
        self.id = id
        self.productCode = productCode
        self.name = name
        self.wholesalePrice = wholesalePrice
        self.retailPrice = retailPrice
        self.description = description

    def __del__(self):
        print(f"Destructor called: Commodity '{self.name}' has been destroyed.")

    def print_info(self):
        print("--- Commodity Information ---")
        print(f"ID: {self.id}")
        print(f"Product Code: {self.productCode}")
        print(f"Name: {self.name}")
        print(f"Wholesale Price: ${self.wholesalePrice}")
        print(f"Retail Price: ${self.retailPrice}")
        print(f"Description: {self.description}")
        print(f"Category (Class Attribute): {self.category}")


# 1. Instantiate the class
item = Commodity(1, "PROD-101", "Wireless Mouse", 15.0, 25.0, "Ergonomic 2.4GHz mouse")

item.warranty_months = 12
print(f"Dynamically added instance attribute (Warranty): {item.warranty_months} months")

Commodity.global_tax_rate = 0.12
print(f"Dynamically added class attribute (Tax Rate): {Commodity.global_tax_rate}")

item.print_info()

print("\nRemoving instance reference...")
del item