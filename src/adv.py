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

# * SET ITEMS HERE FOR ROOMS
room['foyer'].items.append('Overload Potion x 1')
room['foyer'].items.append('Bronze Dagger')
room['overlook'].items.append('Rune Plate (G) Trimmed')
room['narrow'].items.append('torch')
room['treasure'].items.append('Gold')

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

while (kuma.prev_room != None or move == None):

    # * MOVE INDICATOR RESULTS AFTER PROMPTING USER FOR CHOICES.
    move = input("[N] North [E] East [S] South [W] West [Q] Quit \n").lower()

    if move in ['n','e','s','w']:
        kuma.choose(move)

    elif move == 'q':
        # * CHOICE SELECTION MESSAGE.
        print('Selected Choice: Exiting building...')
        exit()
else:
    print('Could not verify user input! Exiting now.')
    exit()
