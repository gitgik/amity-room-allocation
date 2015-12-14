# models.py
class Room(object):
    def __init__(self, dict_of_rooms):
        self.room_dict = dict_of_rooms
        self.members = []

    """ The size of the room """
    def size(self):
        return len(self.members)

    def members_names(self):
        member_list = [member.name for member in self.members]
        return member_list

    """ pre-populate the rooms dictionaries with list of names """
    def populate_room_names(self):
        result = dict([(key, []) for key in self.room_dict])
        return result


class Office(Room):
    maximum_size = 6


class LivingSpace(Room):
    maximum_size = 4

