##Created solely using Copilot, this is the test class for the program.

import unittest
from product import Product
from inventory import Inventory

# Test cases for the Product class
class TestProduct(unittest.TestCase):
    # Test the initialization of a Product instance
    def test_product_init(self):
        product = Product("123", "Test Item", "Category", 10, 1.99)
        self.assertEqual(product.product_id, "123")  # Verify product_id
        self.assertEqual(product.name, "Test Item")  # Verify name
        self.assertEqual(product.category, "Category")  # Verify category
        self.assertEqual(product.quantity, 10)  # Verify quantity
        self.assertEqual(product.price, 1.99)  # Verify price

    # Test the string representation of a Product instance
    def test_product_str(self):
        product = Product("123", "Test Item", "Category", 10, 1.99)
        self.assertIn("Test Item", str(product))  # Check if name is in string representation

# Test cases for the Inventory class
class TestInventory(unittest.TestCase):
    # Set up a fresh Inventory instance and sample products before each test
    def setUp(self):
        self.inventory = Inventory()
        self.productA = Product("001", "Mouse", "Electronics", 5, 19.99)
        self.productB = Product("002", "Keyboard", "Electronics", 2, 29.99)

    # Test adding a product to the inventory
    def test_add_product(self):
        self.inventory.add_product(self.productA)
        self.assertEqual(len(self.inventory.products), 1)  # Check inventory size
        self.assertIn(self.productA.product_id, self.inventory.products)  # Verify product addition

    # Test updating an existing product's details in the inventory
    def test_update_product(self):
        self.inventory.add_product(self.productA)
        self.inventory.update_product("001", name="Gaming Mouse", quantity=10)
        updated = self.inventory.products["001"]
        self.assertEqual(updated.name, "Gaming Mouse")  # Verify name update
        self.assertEqual(updated.quantity, 10)  # Verify quantity update

    # Test deleting a product from the inventory
    def test_delete_product(self):
        self.inventory.add_product(self.productA)
        self.inventory.delete_product("001")
        self.assertNotIn("001", self.inventory.products)  # Ensure product is deleted

    # Test searching for a product by its name
    def test_search_product_by_name(self):
        self.inventory.add_product(self.productA)
        self.inventory.add_product(self.productB)
        results = self.inventory.search_product_by_name("Mouse")
        self.assertEqual(len(results), 1)  # Verify one result is returned
        self.assertIn("Mouse", results[0].name)  # Check if the correct product is found

    # Test checking for products below the reorder threshold
    def test_check_reorder_threshold(self):
        self.inventory.add_product(self.productA)
        self.inventory.add_product(self.productB)
        low_stock = self.inventory.check_reorder_threshold(3)
        self.assertEqual(len(low_stock), 1)  # Verify one product is below threshold
        self.assertIn(self.productB, low_stock)  # Confirm the correct product is identified

if __name__ == '__main__':
    unittest.main()