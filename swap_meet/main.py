class Vendor:

    def __init__(self, inventory = []):
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False

    def get_by_category(self, category):
        picked_items = []
        for item in self.inventory:
            if item.category is category:
                picked_items.append(item)
        return picked_items

class Item:

    def __init__(self, category=""):
        self.category = category

    def __str__(self):
        return "Hello World!"
