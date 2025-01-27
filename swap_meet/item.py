import uuid

class Item:
    def __init__(self, id = None, condition = 0.0):
        if not id:
            id = uuid.uuid4().int
        self.id = id
        self.condition = condition

    def get_category(self):
        if isinstance(self, Item):
            return "Item"
    
    def __str__(self):
        statement = f"An object of type Item with id " + str(self.id) + "."
        print(statement)
        return statement
    
    def condition_description(self):
        if self.condition == 5:
            result = "Top tier! If you don't cop this, I will!"
        elif self.condition <= 2.0:
            result = "Yeahhhh, I don't know about this one."
        elif self.condition < 4:
            result = "I mean, it's aiight."
        elif self.condition < 5:
            result = "A hot commodity!"
        return result 