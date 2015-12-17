# models.py
class Room(object):
    def __init__(self, dict_or_list=None):
        self.room_dict = dict_or_list
        self.unallocated_people = dict_or_list

    def get_room(self, room_name):
        return self.room_dict[room_name]

    def get_room_occupants(self, room_name):
        return self.room_dict[room_name]

    def unallocated(self, unallocated_list):
        self.unallocated_people = unallocated_list
        return self.unallocated_people


class Office(Room):
    """ a class that represents the office space rooms """

    """ the capacity of a given office room """
    capacity = 6

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

    def unallocated(self, unallocated_list):
        self.unallocated_people = unallocated_list
        return self.unallocated_people


class LivingSpace(Room):
    """ a class that represents the living space for fellows """

    """ the capacity of a given office room """
    capacity = 4

    def populate_room_names(self):
        """ living space names """
        living = {
            'Green': [], 'Blue': [], 'Yellow': [], 'Lilac': [],
            'Orange': [], 'White': [], 'Brown': [],
            'Turquoise': [], 'Grey': [], 'Purple': []
        }
        self.room_dict = dict([(key, []) for key in living])
        return self.room_dict

    """ Save the allocated room and their respective occupants """
    def save(self, room_dictionary):
        self.room_dict = room_dictionary
        return self.room_dict

    def unallocated(self, unallocated_list):
        self.unallocated_people = unallocated_list
        return self.unallocated_people
