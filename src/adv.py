# * IMPORTS * #
from room import Room
from player import Player
from items import Items

# Declare all the rooms

room = {
    'outside':  Room(
        "Outside Cave Entrance",
        "North of you, the cave mount beckons"
    ),

    'foyer':    Room(
        "Foyer",
        """
        Dim light filters in from the south. Dusty
        passages run north and east.
        """
    ),

    'overlook': Room(
        "Grand Overlook",
        """
        A steep cliff appears before you, falling
        into the darkness. Ahead to the north, a light flickers in
        the distance, but there is no way across the chasm.
        """
    ),

    'narrow':   Room(
        "Narrow Passage",
        """
        The narrow passage bends here from west
        to north. The smell of gold permeates the air.
        """
    ),

    'treasure': Room(
        "Treasure Chamber",
        """
        You've found the long-lost treasure
        chamber! Sadly, it has already been completely emptied by
        earlier adventurers. The only exit is to the south.
        """
    ),

    'varrock': Room(
        "Varrock City",
        """
        Varrock (originally known as Avarrocka) is one of 
        the largest cities and is also one of the most 
        popular cities in all of RuneScape.
        """
    ),

    'demacia': Room(
        "Demacia City",
        """
        A strong, lawful kingdom with a prestigious military history,
        Demacia’s people have always valued the ideals of justice, honor,
        and duty most highly, and are fiercely proud of their cultural heritage.
        But in spite of these lofty principles, this largely self-sufficient nation
        has grown more insular and isolationist in recent centuries.
            
        Now, Demacia is a kingdom in turmoil.
        """
    ),
}


# * Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']
room['treasure'].w_to = room['varrock']
room['varrock'].n_to = room['demacia']

# * SET ITEMS HERE FOR ROOMS

items = {
    "low_potion": Items('low_potion', 'Heals for 20 HP', 'consumable'),
    "dragon Scimitar": Items('dragon Scimitar', 'Obtained from monkey madness', 'weapon'),
    "abyssal whip": Items('abyssal whip', 'Obtained as a drop from abyssal demons', 'weapon'),
    "overload potion": Items('overload potion', 'Overloads are potions which combine the boosting properties of all 5 extreme potions', 'consumable'),
    "dragon fire shield": Items('dragon fire shield', 'A heavy shield with a snarling, draconic visage.', 'off-hand')
}

room['foyer'].addItem(items["overload potion"])
room['foyer'].addItem(items["dragon Scimitar"])
room['overlook'].addItem(items["abyssal whip"])
room['narrow'].addItem(items["overload potion"])
room['treasure'].addItem(items["dragon fire shield"])

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

    if move in ['n', 'e', 's', 'w']:
        kuma.choose(move)

    elif move == 'q':
        # * CHOICE SELECTION MESSAGE.
        print('Selected Choice: Exiting building...')
        exit()
else:
    print('Could not verify user input! Exiting now.')
    exit()
