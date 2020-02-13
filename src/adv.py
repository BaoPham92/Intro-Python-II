# * IMPORTS * #
from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# * PLAYER CLASS INSTANTIATION.
kuma = Player(
    'Kuma',
    'I am a newbie from Varrock who came from Lumbridge and Farrock',
    room['outside']
)

# * MOVE PLACEHOLDER
move = None

# * TEMPLATE FOR RETURNING A MESSAGE FOR USER'S CHOOSING A DESTINATION.
def choosingPathMessage():
        if (kuma.room and kuma.prevRoom): 
            print(F'You are now in {kuma.room.name} room.\nDescription: {kuma.room.info} \nPreviously, you were in {kuma.prevRoom.name}')

        elif (kuma.room):
            print(F'You are now in {kuma.room.name} room.\nDescription: {kuma.room.info}')
        else: 
            print('Could not detect room! You fall into a never ending dark hole!!') 
            exit()

while (not hasattr(kuma, 'prevRoom') == None or move == None):

    # * MOVE INDICATOR RESULTS AFTER PROMPTING USER FOR CHOICES.
    move = input("[0] North [1] East [2] South [3] West [Q] Quit \n")

    # * CONFIRM AND OR CONVERT CHOICES TO INTEGERS
    if (move == 'Q' or move == 'q'):
        print(F'You have chosen {move}')
    else:
        move = int(move)
        print(F'You selected option: {move}')

    if move == 0 and hasattr(kuma.room, 'n_to'):
        # * CHOICE SELECTION MESSAGE, AND ROOM CHANGE.
        kuma.prevRoom = kuma.room
        kuma.room = kuma.room.n_to
        choosingPathMessage()

    elif move == 1 and hasattr(kuma.room, 'e_to'):
        # * CHOICE SELECTION MESSAGE, AND ROOM CHANGE.
        kuma.prevRoom = kuma.room
        kuma.room = kuma.room.e_to
        print(F'DEFNITELY 1 {kuma.prevRoom.name}')
        choosingPathMessage()

    elif move == 2 and hasattr(kuma.room, 's_to'):
        # * CHOICE SELECTION MESSAGE, AND ROOM CHANGE.
        kuma.prevRoom = kuma.room
        kuma.room = kuma.room.s_to
        choosingPathMessage()

    elif move == 3 and hasattr(kuma.room, 'w_to'):
        # * CHOICE SELECTION MESSAGE, AND ROOM CHANGE.
        kuma.prevRoom = kuma.room
        kuma.room = kuma.room.w_to
        choosingPathMessage()

    elif move == 'Q' or move == 'q':
        # * CHOICE SELECTION MESSAGE.
        print('Selected Choice: Exiting building...')
        exit()
else:
    print('Could not verify user input! Exiting now.')
    exit()
