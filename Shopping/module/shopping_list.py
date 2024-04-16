import re
class ShoppingList:
    """
    A class to represent a list of items to buy.
    """
    def __init__(self):
        """
        Initialize the list of items to buy.
        """
        self.items = []

    def add_item(self, id, name, price,  quantity):
        """
        Add an item to the list.
        :param str id: The id of product is unique 8 character string with numbers and upper case letters.
        :param str name: The name of product is a string.
        :param float price: The price of product is floating point number.
        :param int quantity: The quantity of product is integer.
        :return: None.

        """
        self.items.append({
            'id': id,
            'name': name,
            'price': price,
            'quantity': quantity
        })    

    def remove_item(self, id):
        """
        Remove an item from the list.
        :param str id: The id of product is unique 8 character string with numbers and upper case letters.
        :return: None.
        """
        for item in self.items:
            if item['id'] == id:
                self.items.remove(item)
                break

    def add_multiple_items(self, items):
        """
        Add multiple items to the list.
        :param list items: A list of items to add.
        :return: None.
        """
        self.items.extend(items)         

    def remove_multiple_items(self, ids):
        """
        Remove multiple items from the list.
        :param list ids: A list of ids of items to remove.
        :return: None.
        """
        for id in ids:
            self.remove_item(id)  

    def is_product_id_valid(self, id):
        """
        Check if the product id is valid.
        :param str id: The id of product is unique 8 character string with numbers and upper case letters.
        :return: True if the id is valid, False otherwise.
        """
        return bool(re.match(r'^[A-Z0-9]{8}$', id))         

   