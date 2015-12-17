# models.py
class Room(object):
    def __init__(self, dict_of_rooms=None):
        self.room_dict = dict_of_rooms
        self.unalloc_people = []

    def get_room(self, room_name):
        return self.room_dict[room_name.lower()]

    def get_room_occupants(self, room_name):
        """ get the occupants of a specific room """
        return self.room_dict[room_name.lower()]

    def unallocated_people(self, unallocated_list):
        if len(unallocated_list) > 0:
            self.unalloc_people = unallocated_list
            return self.unalloc_people
        else:
            return False

    def get_unallocated_people(self):
        return self.unalloc_people


class Office(Room):
    """ a class that represents the office space rooms """

    """ the capacity of a given office room """
    capacity = 1

    def populate_room_names(self):
        office = {
            "allegro": [], "boma": [], "valhalla": [],
            "hogwarts": [], "krypton": [], "oculus": [],
            "gondolla": [], "amitoid": [], "punta": [], "borabora": []
        }
        self.room_dict = dict([(key, []) for key in office])
        return self.room_dict

    """ Save the allocated room and their respective occupants """
    def save(self, room_dictionary):
        self.room_dict = room_dictionary
        return self.room_dict


class LivingSpace(Room):
    """ a class that represents the living space for fellows """

    """ the capacity of a given office room """
    capacity = 4

    def populate_room_names(self):
        """ living space names """
        living = {
            'green': [], 'blue': [], 'yellow': [], 'lilac': [],
            'orange': [], 'white': [], 'brown': [],
            'turquoise': [], 'grey': [], 'purple': []
        }
        self.room_dict = dict([(key, []) for key in living])
        return self.room_dict

    """ Save the allocated room and their respective occupants """
    def save(self, room_dictionary):
        self.room_dict = room_dictionary
        return self.room_dict
