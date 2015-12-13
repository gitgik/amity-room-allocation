# models.py
class Room(object):
    def __init__(self, list_of_rooms):
        self.list = list_of_rooms
        self.members = []

    # The size of the room
    def size(self):
        return len(self.members)

    def members_names(self):
        member_list = [member.name for member in self.members]
        return member_list

    # pre-populate the rooms with names
    def populate_room_names(self):
        room_names = []
        for i in self.list:
            room_names.append(i)
        return room_names


class Office(Room):
    maximum_size = 6


class LivingSpace(Room):
    maximum_size = 4

