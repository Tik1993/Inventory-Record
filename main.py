import json

from database import Database
from item import Item


database = Database()

with open("items.json","r",encoding="utf-8") as f:
    items = json.load(f)

database.load_data(items)
