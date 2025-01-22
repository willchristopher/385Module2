class Product:
    def __init__(self, product_id, name, category, quantity, price):
        # Constructor method to initialize the Product object with given attributes
        self.product_id = product_id  # Unique identifier for the product
        self.name = name  # Name of the product
        self.category = category  # Category to which the product belongs
        self.quantity = quantity  # Quantity of the product available
        self.price = price  # Price of the product

    def __str__(self):
        # String representation method to return a formatted string with product details
        return f"ID: {self.product_id}, Name: {self.name}, Category: {self.category}, Quantity: {self.quantity}, Price: {self.price}"