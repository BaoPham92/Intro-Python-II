# Write a class to hold player information, e.g. what room they are in
# currently.

# * PLAYER TEMPLATE FOR INSTANTIATIONS.
class Player():
    def __init__(self, name, bio, room):
        self.name = name
        self.bio = bio
        self.room = room
        self.prev_room = None
        self.bag = []
        self.mainEquipment = 'Zamorak God Sword'
        self.offHand = ''
        self.skills = []

    def __str__(self):
        return F' Welcome, {self.name}. \n A little about you: {self.bio}. \n You current have {len(self.bag)} items in your bag. \n You are currently in the {self.room} part of this building, how do you move forward?'

    @staticmethod
    # * CHECK FOR ITEMS & PRESENT USER OPTIONS OF INTERACTION
    def item_interaction(self):
        if (self.room.items[0] != None or []):
            itemChoice = input(F'You notice there is an object within this room, it\'s a {self.room.items[0]} \n [G] choose to grab item? [N] No.\n').lower()

            if (itemChoice == 'g'):
                self.bag.append(self.room.items[0])
                self.room.items.remove(self.room.items[0])

                if (self.bag != [] or self.bag != None):
                    for item in self.bag:
                        print(F'Currently your bag has: {item}')
                if (self.room.items == [] or self.room.items == None):
                    print('There are now no more items in the room!')
        else: pass

    @staticmethod
    # * TEMPLATE FOR RETURNING A MESSAGE FOR USER'S CHOOSING A DESTINATION.
    def choosingPathMessage(self):
        if (self.prev_room != None and self.room):
            print(F'You are now in {self.room.name} room.\nDescription: {self.room.info} \nPreviously, you were in {self.prev_room.name}')

        else:
            print(F'You are now in {self.room.name} room.\nDescription: {self.room.info}')

    # * PLAYER CHOOSES ROOM & SET PREVIOUS ROOM
    def choose(self, choice):
        # * NEXT ROOM CONTAINER
        new_room = getattr(self.room, F'{choice}_to')

        if (choice != None and new_room != None):
            # * ROOM CHANGE.
            self.prev_room = self.room
            self.room = new_room
            self.choosingPathMessage(self)
            self.item_interaction(self)
        else:
            print('There is no room in that direction!')
