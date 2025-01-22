

# main.py

from inventory import Inventory  # Importing the Inventory class from inventory module
from product import Product  # Importing the Product class from product module

def main():
    inventory = Inventory()  # Creating an instance of Inventory

    while True:
        # Displaying the menu options to the user
        print("\nInventory Management System")
        print("1. Add Product")
        print("2. Update Product")
        print("3. Delete Product")
        print("4. View Inventory")
        print("5. Exit")
        choice = input("Enter your choice: ")  # Taking user input for menu choice

        if choice == '1':
            # Adding a new product
            product_id = input("Enter product ID: ")  # Taking product ID input
            name = input("Enter product name: ")  # Taking product name input
            category = input("Enter product category: ")  # Taking product category input
            quantity = int(input("Enter product quantity: "))  # Taking product quantity input and converting to integer
            price = float(input("Enter product price: "))  # Taking product price input and converting to float
            product = Product(product_id, name, category, quantity, price)  # Creating a Product object
            inventory.add_product(product)  # Adding the product to the inventory
        elif choice == '2':
            # Updating an existing product
            product_id = input("Enter product ID to update: ")  # Taking product ID input for the product to update
            name = input("Enter new name (leave blank to keep current): ")  # Taking new name input (optional)
            category = input("Enter new category (leave blank to keep current): ")  # Taking new category input (optional)
            quantity = input("Enter new quantity (leave blank to keep current): ")  # Taking new quantity input (optional)
            price = input("Enter new price (leave blank to keep current): ")  # Taking new price input (optional)
            # Updating the product in the inventory with new values or keeping current values if left blank
            inventory.update_product(product_id, name or None, category or None, int(quantity) if quantity else None, float(price) if price else None)
        elif choice == '3':
            # Deleting a product
            product_id = input("Enter product ID to delete: ")  # Taking product ID input for the product to delete
            inventory.delete_product(product_id)  # Deleting the product from the inventory
        elif choice == '4':
            # Viewing the inventory        elif choice == '4':
            inventory.view_inventory()#method to view the inventory