from product import Product

class Inventory:
    def __init__(self):
        # Constructor method to initialize the Inventory object with an empty dictionary of products
        self.products = {}

    def add_product(self, product):
        # Method to add a product to the inventory
        self.products[product.product_id] = product

    def update_product(self, product_id, name=None, category=None, quantity=None, price=None):
        # Method to update an existing product's details in the inventory
        if product_id in self.products:
            if name:
                self.products[product_id].name = name
            if category:
                self.products[product_id].category = category
            if quantity is not None:
                self.products[product_id].quantity = quantity
            if price is not None:
                self.products[product_id].price = price
        else:
            print("Product not found.")

    def delete_product(self, product_id):
        # Method to delete a product from the inventory
        if product_id in self.products:
            del self.products[product_id]
        else:
            print("Product not found.")

    def search_product_by_name(self, name_query):
        # Method to search for products by name in the inventory
        results = []
        for product_id, product in self.products.items():
            if name_query.lower() in product.name.lower():
                results.append(product)
        return results

    def check_reorder_threshold(self, threshold=5):
        # Method to check for products with quantity below a specified threshold
        low_stock_products = []
        for product in self.products.values():
            if product.quantity < threshold:
                low_stock_products.append(product)
        return low_stock_products

    def view_inventory(self):
        # Method to display the current inventory
        if not self.products:
            print("Inventory is empty.")
            return
        print("\nCurrent Inventory:")
        print(f"{'ID':<10}{'Name':<20}{'Category':<15}{'Quantity':<10}{'Price':<10}")
        print("-" * 65)
        for product in self.products.values():
            print(f"{product.product_id:<10}{product.name:<20}{product.category:<15}{product.quantity:<10}{product.price:<10.2f}")