class Vendor:
    def __init__(self, inventory=None):
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
    
    def swap_first_item(self, other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False
        return self.swap_items(other_vendor, self.inventory[0], other_vendor.inventory[0])
        
        
    def get_by_category(self, category):
        if self.inventory == []:
            return []
        else:
            return [item for item in self.inventory if item.get_category()==category]
        
    def get_best_by_category(self, category):
        best = None
        temp_high_condition =-1
        for item in self.inventory:
            if item.get_category() == category and item.condition > temp_high_condition:
                temp_high_condition = item.condition
                best = item
        return best
    
    
    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        my_best = self.get_best_by_category(their_priority)
        their_best = other_vendor.get_best_by_category(my_priority)

        if not my_best or not their_best:
            return False
        
        return self.swap_items(other_vendor, my_best, their_best)
            
      
        
            


        
        
