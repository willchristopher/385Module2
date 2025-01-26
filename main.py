#Will Christopher CSC 385
#Main file to run the Inventory Management System.

from inventory import Inventory  # Import the Inventory class from the inventory module
from product import Product      # Import the Product class from the product module

def main():
    """Main function to run the Inventory Management System."""
    
    # Create an instance of Inventory to manage products
    inventory = Inventory()

    # Add some example items to the inventory
    inventory.add_product(Product("1001", "Wireless Mouse", "Electronics", 10, 19.99))
    inventory.add_product(Product("1002", "Water Bottle", "Kitchen", 3, 9.99))

    while True:
        # Display the menu options to the user
        print("\nInventory Management System")
        print("1. Add Product")
        print("2. Update Product")
        print("3. Delete Product")
        print("4. View Inventory")
        print("5. Exit")
        print("6. Search Product by Name")
        print("7. Check Low Stock")
        
        # Prompt the user to enter their choice
        choice = input("Enter your choice: ")

        if choice == '1':
            # Handle adding a new product
            product_id = input("Enter product ID: ")
            name = input("Enter product name: ")
            category = input("Enter product category: ")
            
            try:
                # Convert quantity and price to appropriate data types
                quantity = int(input("Enter product quantity: "))
                price = float(input("Enter product price: "))
            except ValueError:
                # Handle invalid input for quantity or price
                print("Invalid input for quantity or price. Please enter numeric values.")
                continue  # Restart the loop

            # Create a new Product instance with the provided details
            product = Product(product_id, name, category, quantity, price)
            
            # Add the new product to the inventory
            inventory.add_product(product)
            print(f"Product '{name}' added successfully.")

        elif choice == '2':
            # Handle updating an existing product
            product_id = input("Enter product ID you would like to update: ")
            name = input("Enter new name (leave blank to keep current name): ")
            category = input("Enter new category (leave blank to keep current category): ")
            quantity_input = input("Enter new quantity (leave blank to keep current): ")
            price_input = input("Enter new price (leave blank to keep current): ")

            try:
                # Convert quantity and price if new values are provided
                quantity = int(quantity_input) if quantity_input else None
                price = float(price_input) if price_input else None
            except ValueError:
                # Handle invalid input for quantity or price
                print("Invalid input for quantity or price. Please enter numeric values.")
                continue  # Restart the loop

            # Update the product in the inventory with the new details
            inventory.update_product(
                product_id,
                name or None,
                category or None,
                quantity,
                price
            )
            print(f"Product ID '{product_id}' updated successfully.")

        
        elif choice == '3':
            # Handle deleting a product
            product_id = input("Enter product ID to delete: ")
            inventory.delete_product(product_id)
            print(f"Product ID '{product_id}' deleted successfully.")

        elif choice == '4':
            # Handle viewing the entire inventory
            inventory.view_inventory()

        elif choice == '5':
            # Handle exiting the program
            print("Exiting the Inventory Management System. Goodbye!")
            break  # Exit the while loop to terminate the program

        elif choice == '6':
            # Handle searching for a product by name
            query = input("Enter product name to search: ")
            found = inventory.search_product_by_name(query)
            if found:
                print("\nSearch Results:")
                for p in found:
                    print(p)
            else:
                print("No products found matching the search criteria.")

        elif choice == '7':
            # Handle checking for low stock products
            try:
                threshold = int(input("Enter stock threshold: "))
            except ValueError:
                # Handle invalid input for threshold
                print("Invalid input for threshold. Please enter a numeric value.")
                continue  # Restart the loop

            low_stock = inventory.check_reorder_threshold(threshold)
            if low_stock:
                print(f"\nProducts with stock below {threshold}:")
                for item in low_stock:
                    print(item)
            else:
                print("No products are below the specified threshold.")

        else:
            # Handle invalid menu choices
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()  # Call the main function to start the program