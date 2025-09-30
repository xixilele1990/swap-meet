import uuid

class Item:
    def __init__(self, id = None, condition = 0):
        if id is None:
            self.id = uuid.uuid4().int
        else:
            self.id = id
        self.condition = condition

    def get_category(self):
        return "Item"
    
    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}."
    
    def condition_description(self):
        if self.condition == 5:
            return "New"
        elif self.condition == 4:
            return "Like New"
        elif self.condition == 3:
            return "Good"
        elif self.condition == 2:
            return "Fair"
        elif self.condition == 1:
            return "Poor"
        else:
            return "Unknown"