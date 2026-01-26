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

