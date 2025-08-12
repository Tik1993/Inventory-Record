import random
class Item:
    def __init__(self,  name, category, brand, year, id = None):
        self.id = id if id is not None else random.randint(0,99999)
        self.name = name
        self.category=category
        self.brand = brand
        self.year = year

    def __repr__(self):
        return f"The item '{self.name}' with id { self.id} belongs to category '{self.category}'. Its brand {self.brand} and year: {self.year}"
    

