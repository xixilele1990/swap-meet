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

    def swap_first_item(self, other):
        if len(self.inventory) and len(other.inventory):
            my_first_item = self.remove(self.inventory[0])
            their_first_item = other.remove(other.inventory[0])
            self.add(their_first_item)
            other.add(my_first_item)
            return True
        else:
            return False

class Item:

    def __init__(self, category=""):
        self.category = category

    def __str__(self):
        return "Hello World!"

class Clothing(Item):
    def __init__(self):
        self.category = "Clothing"
    def __str__(self):
        return "The finest clothing you could wear."

class Decor(Item):
    def __init__(self):
        self.category = "Decor"
    def __str__(self):
        return "Something to decorate your space."

class Electronics(Item):
    def __init__(self):
        self.category = "Electronics"
    def __str__(self):
        return "A gadget full of buttons and secrets."
