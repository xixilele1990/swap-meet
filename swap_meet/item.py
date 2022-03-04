class Item:
    def __init__(self, condition=0, category=''):
        self.category = category
        self.condition = condition

    def __str__(self):
        return "Hello World!"

    def longest_description(self):
        return "implemented in child"

    def condition_description(self):
        if self.condition > 3:
            return "It's great!"
        else:
            return "It stinks!"





