# Write a class to hold player information, e.g. what room they are in
# currently.

# * PLAYER TEMPLATE FOR INSTANTIATIONS.
class Player():
    def __init__(self, name, bio, room='entrance'):
        self.name = name
        self.bio = bio
        self.room = room
        self.bag = []
        self.mainEquipment = 'Zamorak God Sword'
        self.offHand = ''
        self.skills = []

    def __str__(self):
        return F' Welcome, {self.name}. \n A little about you: {self.bio}. \n You current have {len(self.bag)} items in your bag. \n You are currently in the {self.room} part of this building, how do you move forward?'