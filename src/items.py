 # * ITEM CLASS
class Items():

    def __init__(self, name, description, type):
        self.name = name
        self.description = description
        self.type = type

    def __str__(self):
        return F'Item: {self.name}, Description: {self.description}'
