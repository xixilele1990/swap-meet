from swap_meet.item import Item

class Decor(Item):
    def __init__(self, condition=None):
        super().__init__(condition=condition, category='Decor')

    def __str__(self):
        return "Something to decorate your space."

    def long_description(self):
        if self.condition > 4.0:
            print("Very good condition")
        elif 3.0 < self.condition <= 4.0:
            print("Pretty good condition")
        elif  2.0 < self.condition <= 3.0:
            print("Noticeable wear and tear")
        else:
            print("Fashionably rustic")