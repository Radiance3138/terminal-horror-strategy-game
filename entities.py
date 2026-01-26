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
    
class Character:
    def __init__(self, name, location, inventory, panic_level, dialogue_options, is_player=False):
        """
        Docstring for __init__
        
        :string name: The name of the character.
        :Bool is_player: Indicates if the character is the player or NPC.
        :room_object location: The current location of the character (Room object).
        :list inventory: List of items the character possesses (Item objects).
        :int panic_level: The panic level of the character (0-100).
        :dict dialogue_options: Dialogue options available for interaction.
        """

        self.name = name
        self.is_player = is_player
        self.location = location 
        self.inventory = inventory
        self.panic_level = panic_level
        self.dialogue_options = dialogue_options 

    def move_to(self, direction):
        """Moves the character to a neighboring room in the specified direction.
        
        :room_object direction: The direction to move (e.g., 'north', 'south', etc.).
        """

        if direction.lower() in self.location.neighbors:
            self.location = self.location.neighbors[direction.lower()]
            return True
        
        return False
        