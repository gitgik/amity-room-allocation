# models.py
class Room(object):
    space = {}

    def __init__(self, dict_of_rooms):
        self.room_dict = dict_of_rooms
        self.members = []

    """ The size of the room """
    def size(self):
        return len(self.members)

    def members_names(self, room_name):
        # member_list = [member for member in self.members]
        return self.space[room_name]

    """ pre-populate the rooms dictionaries with list of names """
    def populate_room_names(self):
        self.room_dict = dict([(key, []) for key in self.room_dict])
        return self.room_dict


class Office(Room):
    maximum_size = 6


class LivingSpace(Room):
    maximum_size = 4

