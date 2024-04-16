import unittest
from shopping_list import ShoppingList

class ShoppingListTest(unittest.TestCase):
    def test_add_item(self):
        shopping_list = ShoppingList()
        shopping_list.add_item("1234ABCD","Milk", 1.50, 1)
        self.assertEqual(shopping_list.items, [{"id": "1234ABCD", "name": "Milk", "price": 1.50, "quantity": 1}]) 

    def test_remove_item(self):
        shopping_list = ShoppingList()
        shopping_list.add_item("1234ABCD","Milk", 1.50, 1)
        shopping_list.remove_item("1234ABCD")
        self.assertEqual(shopping_list.items, [])    

    def test_add_multiple_items(self):
        shopping_list = ShoppingList()
        list_of_items = [
            {"id": "1234ABCD", "name": "Milk", "price": 1.50, "quantity": 1},
            {"id": "5678EFGH", "name": "Eggs", "price": 2.00, "quantity": 2},
            {"id": "9012IJKL", "name": "Bread", "price": 3.00, "quantity": 3},
            {"id": "3456MNOP", "name": "Cheese", "price": 4.00, "quantity": 4}
        ]
        shopping_list.add_multiple_items(list_of_items)
        self.assertEqual(shopping_list.items, list_of_items)

    def test_remove_multiple_items(self):
        shopping_list = ShoppingList()
        list_of_items = [
            {"id": "1234ABCD", "name": "Milk", "price": 1.50, "quantity": 1},
            {"id": "5678EFGH", "name": "Eggs", "price": 2.00, "quantity": 2},
            {"id": "9012IJKL", "name": "Bread", "price": 3.00, "quantity": 3},
            {"id": "3456MNOP", "name": "Cheese", "price": 4.00, "quantity": 4}
        ]
        shopping_list.add_multiple_items(list_of_items)
        shopping_list.remove_multiple_items(["1234ABCD", "5678EFGH"])
        self.assertEqual(shopping_list.items, [{"id": "9012IJKL", "name": "Bread", "price": 3.00, "quantity": 3}, {"id": "3456MNOP", "name": "Cheese", "price": 4.00, "quantity": 4}])    
    

    def test_is_product_id_valid(self):
        shopping_list = ShoppingList()
        list_valid_product_ids = ["1234ABCD", "5678EFGH", "9012IJKL", "3456MNOP"]
        list_invalid_product_ids = ["1234ABC", "5678EFG", "9012IJK", "3456MNO"]
        for product_id in list_valid_product_ids:
            self.assertTrue(shopping_list.is_product_id_valid(product_id))

        for product_id in list_invalid_product_ids:
            self.assertFalse(shopping_list.is_product_id_valid(product_id))