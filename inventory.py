from product import Product  # Importing the Product class from product module

class Inventory:
    def __init__(self):
        # Constructor method to initialize the Inventory object with an empty dictionary of products
        self.products = {}

    def add_product(self, product):
        # Method to add a product to the inventory
        self.products[product.product_id] = product  # Adding the product to the dictionary with product_id as the key

    def update_product(self, product_id, name=None, category=None, quantity=None, price=None):
        # Method to update an existing product's details in the inventory
        if product_id in self.products:
            # If the product exists in the inventory, update its details
            if name:
                self.products[product_id].name = name  # Update name if provided
            if category:
                self.products[product_id].category = category  # Update category if provided
            if quantity:
                self.products[product_id].quantity = quantity  # Update quantity if provided
            if price:
                self.products[product_id].price = price  # Update price if provided
        else:
            # If the product does not exist, print an error message
            print("Product not found.")

    def delete_product(self, product_id):
        # Method to delete a product from the inventory
        if product_id in self.products:
            del self.products[product_id]  # Remove the product from the dictionary
        else:
            # If the product does not exist, print an error message
            print("Product not found.")

    def view_inventory(self):
        # Method to view all products in the inventory
        for product in self.products.values():
            print(product)  # Print the string representation of each product