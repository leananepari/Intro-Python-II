# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:

  def __init__(self, room):
    self.room = room
    self.items = []

  def move(self, direction):

    if getattr(self.room, f"{direction}_to"):
      self.room = getattr(self.room, f"{direction}_to")
    else:
      print('Movement is not allowed')
  
  def getItem(self, item):
    itemObj = None
    for x in range(len(self.room.items)):
      if self.room.items[x].name == item:
        itemObj = self.room.items[x].name
        self.items.append(self.room.items[x])
        del(self.room.items[x])
        break
    if itemObj == None:
      print('No such item')
    else:
      print(f"You picked up {itemObj}")
