from swap_meet.item import Item

class Electronics(Item):
    def __init__(self, condition=0):
        super().__init__(condition, category='Electronics')
        #Item(condition, category="Electronics")
        #self.condition = condition
        #self.category = "Electronics"

    def __str__(self):
        return "A gadget full of buttons and secrets."

