# models.py
class Room(object):
    def __init__(self, dict_of_rooms):
        self.room_dict = dict_of_rooms

    def members_names(self, room_name):
        return self.room_dict[room_name]

    """ pre-populate the rooms dictionaries with list of names """
    def populate_room_names(self):
        self.room_dict = dict([(key, []) for key in self.room_dict])
        return self.room_dict


class Office(Room):
    maximum_size = 6


class LivingSpace(Room):
    maximum_size = 4

