from player import Player
from room import Room
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

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

print("Welcome!!!")

name = input("Player name: ")

location = room['outside']

player = Player(name, location)

print(f"Hello {name}, standing at {location}")
print("press '1' to go north, '2' to go south, '3' to go east, '4' to go west, 'q' to quit")
print("Have fun!!!")

print(location)

def choose_action():
    return int(input("[1] north  [2] south   [3] east  [4] west    [9] Quit\n"))


action = choose_action()


def next_step():
    print(location)
    print('where would you like to go next?')
    global action
    action = choose_action()


def wrong_way():
    print('that direction is blocked, try again')
    global action
    action = choose_action()


while not action == 9:
    if location == room['outside']:
        if action == 1:
            location = room['outside'].n_to
            next_step()
        else:
            location == room['outside']
            print('wrong way')
            next_step()
    elif location == room['foyer']:

        if action == 2:
            location = room['foyer'].s_to
            next_step()
        
        elif action == 3:
            location = room['foyer'].e_to
            next_step()

        elif action == 1:
            location = room['foyer'].n_to
            next_step()
        else:
            location == room['foyer']
            print('wrong way')
            next_step()

    elif location == room['overlook']:
        if action == 2:
            location = room['overlook'].s_to
            next_step()
        else:
            location == room['overlook']
            print('wrong way')
            next_step()

    elif location == room['narrow']:
        if action == 4:
            location = room['narrow'].w_to
            next_step()
        elif action == 1:
            location = room['narrow'].n_to
            next_step()
        else:
            location == room['narrow']
            print('wrong way')
            next_step()

    elif location == room['treasure']:
        if action == 2:
            location = room['treasure'].s_to
            next_step()
        else:
            location == room['treasure']
            print('wrong way')
            next_step()

    else:
        wrong_way()