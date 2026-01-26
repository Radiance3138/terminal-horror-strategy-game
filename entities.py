# defining entities for the game

class Room:
    def __init__(self, name, description):

        self.name = name
        self.description = description
        self.items = {} # item objects in the room
        self.neighbors = {} # neighboring rooms

    def add_neighbor(self, direction, room_object):
        """Adds a neighboring room in the specified direction. The player can choose to move to any neighboring room.

        :key direction: The direction of the neighboring room (e.g., 'north', 'south', etc.).
        :value room_object: The neighboring Room object.
        """

        self.neighbors[direction.lower()] = room_object

    def add_item(self, item_object):
        """The room takes ownership of the item."""
        
        self.items[item_object.name.lower()] = item_object

class Item:
    def __init__(self, name, descriptions, is_portable=True):

        self.name = name
        self.descriptions = descriptions 
        self.current_desc_index = 0
        self.is_portable = is_portable

    def examine(self):
        """Cycles through item descriptions or returns the last one."""
        
        desc = self.descriptions[self.current_desc_index]
        
        if self.current_desc_index < len(self.descriptions) - 1:
            self.current_desc_index += 1
        
        return desc