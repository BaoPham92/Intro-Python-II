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
    def addItem(self, item):
        self.bag.append(item)

    @staticmethod
    def removeItem(self, item):
        self.bag.remove(item)

    @staticmethod
    # * TEMPLATE FOR RETURNING A MESSAGE FOR USER'S CHOOSING A DESTINATION.
    def choosingPathMessage(self):
        # ? PLACEHOLDER FOR A COPY OF LISTED ITEMS IN A ROOM
        item_list_copy = None

        # ? IF ROOM HAS ITEMS, CREATE A COPY FOR LOGIC IN USER SELECTION OF ITEMS
        if (len(self.room.items) > 0):
            item_list_copy = self.room.items.copy()

        # * WHILE CHOOSING PATH, IF ITEMS EXIST LOOP ITEMS
        while (item_list_copy != None and len(item_list_copy) > 0): 

            for item in self.room.items:
                # * PRESENT PLAYER ITEMS AND CHOICES.
                print(F'You notice an item in the room, ITEM: \"{item.name}\" DESCRIPTION: \"{item.description}\" TYPE: \"{item.type}\""')
                choice = input(F'[G] Grab Item? [N] No.').lower()

                # * VALIDATION FOR USER OPTIONS
                if (choice == 'g'):
                    self.addItem(self, item)
                    self.room.removeItem(item)
                    item_list_copy.remove(item)
                    print(F'Current items in your bag: {self.bag}')
                elif (choice == 'n'):
                    item_list_copy.remove(item)
                    print('You decided not to take item.')
                else: print('Valid choices are [G] or [N]')

        if (self.prev_room != None and self.room):
            print(F'You are now in {self.room.name} room.\nDescription: {self.room.info} \nPreviously, you were in {self.prev_room.name} \n')

        else:
            print(F'You are now in {self.room.name} room.\nDescription: {self.room.info} \n')

    # * PLAYER CHOOSES ROOM & SET PREVIOUS ROOM
    def choose(self, choice):
        # * NEXT ROOM CONTAINER
        new_room = getattr(self.room, F'{choice}_to')

        if (choice != None and new_room != None):
            # * ROOM CHANGE.
            self.prev_room = self.room
            self.room = new_room
            self.choosingPathMessage(self)
        else:
            print('There is no room in that direction!')
