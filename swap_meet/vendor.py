class Vendor:
    def __init__(self, inventory = None ):
        self.inventory = [] if inventory is None else inventory
    
    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
        else:
            return False
        return item
    
    def get_by_id(self, num):
        for item in self.inventory:
            if item.id == num:
                return item
        return None
    
    def swap_items(self, other_vendor,  my_item, their_item):
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        else:
            removed_item = self.remove(my_item)
            other_vendor.add(removed_item)
            self.add(other_vendor.remove(their_item))
        return True



        
        
