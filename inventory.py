from product import Product

class Inventory:
    def __init__(self):
        # Constructor method to initialize the Inventory object with an empty dictionary of products
        self.products = {}
        self.name_index = {}  # new dictionary for name-based lookups

    def add_product(self, product):
        # Method to add a product to the inventory
        self.products[product.product_id] = product
        self.name_index[product.name.lower()] = product.product_id  # maintain name-based dict

    def update_product(self, product_id, name=None, category=None, quantity=None, price=None):
        # Method to update an existing product's details in the inventory
        if product_id in self.products:
            old_name = self.products[product_id].name.lower()
            if name:
                # Remove old reference from name_index
                if old_name in self.name_index:
                    del self.name_index[old_name]
                # Add updated reference
                self.name_index[name.lower()] = product_id
            if name:
                self.products[product_id].name = name
            if category:
                self.products[product_id].category = category
            if quantity is not None:
                self.products[product_id].quantity = quantity
            if price is not None:
                self.products[product_id].price = price
        else:
            print("Product was not found.")

    def delete_product(self, product_id):
        # Method to delete a product from the inventory
        if product_id in self.products:
            del self.products[product_id]
        else:
            print("Product was not found.")

    def search_product_by_name(self, name_query):
        # Attempt direct lookup for speed
        product_id = self.name_index.get(name_query.lower())
        if product_id:
            return [self.products[product_id]]
        # Fallback to partial match
        results = []
        for nm in self.name_index:
            if name_query.lower() in nm:
                results.append(self.products[self.name_index[nm]])
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
            print("Inventory is currently empty.")
            return
        print("\nCurrent Inventory:")
        print(f"{'ID':<10}{'Name':<20}{'Category':<15}{'Quantity':<10}{'Price':<10}")
        print("-" * 65)
        for product in self.products.values():
            print(f"{product.product_id:<10}{product.name:<20}{product.category:<15}{product.quantity:<10}{product.price:<10.2f}")