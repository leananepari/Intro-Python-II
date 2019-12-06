from room import Room
from player import Player
from item import Item

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
chamber! Be careful, don't wake the dragon!"""),
}

item = {
  'rock': Item("rock", "Use this rock to break into locked box inside the foyer room"),
  'map': Item("map", "Map to find the treasure room"),
  'flute': Item("flute", "Play flute to make dragon go back to sleep"),
  'key': Item("key", "Use this key to unlock the door to narrow room"),
  'coins': Item("coins", "Collect golden coins if you trick the dragon")
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['outside'].items.append(item['rock'])
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['foyer'].items.append(item['map'])
room['foyer'].items.append(item['flute'])
room['overlook'].s_to = room['foyer']
room['overlook'].items.append(item['key'])
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']
room['treasure'].items.append(item['coins'])


# print(room['outside'].n_to.name)
# print(room['outside'])

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
new_player = Player(room['outside'])

# Write a loop that:
#
while True:
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
  print(new_player.room.name)
  print(new_player.room.description)
  new_player.room.printItems()
# * Waits for user input and decides what to do.
#
  direction = input('go to -> ')
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
  if direction.split(' ')[0] == 'take' or direction.split(' ')[0] == 'get':
    new_player.getItem(direction.split(' ')[1])
  elif direction.split(' ')[0] == 'drop':
    new_player.dropItem(direction.split(' ')[1])
  else:
    if direction == 'n':
      new_player.move('n')
    elif direction == 's':
      new_player.move('s')
    elif direction == 'e':
      new_player.move('e')
    elif direction == 'w':
      new_player.move('w')
    elif direction == 'q':
      print('Goodbye')
      break
    else:
      print('Invalid command')
