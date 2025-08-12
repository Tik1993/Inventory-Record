from item import Item
from typing import List

class Database:
    def __init__(self):
        self.items : List[Item] =[]
    
    def add_item(self, item:Item):
        self.items.append(item)
    
    def remove_item(self, item_id:int):
        self.items = [item for item in self.items if item.id != item_id]

    def list_all(self):
        return self.items
    
    def load_data(self, items):
        for item in items:
            self.add_item(Item(name = item["name"], category=item["category"], brand=item["brand"], year=item["year"], id= item.get("id",None)))