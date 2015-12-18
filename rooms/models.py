# !/usr/bin/python
# title          :amity/alloc.py
# description    :An algorithm which randomly allocates
#                 persons to rooms in a building.
# author         :Jee Githinji
# email          :githinji.gikera@andela.com
# date           :20151218
# version        :0.0.1
# python_version :2.7.10
# ==============================================================================


class Room(object):
    """ this class represents a room in a building """
    def __init__(self, dict_of_rooms=None):
        self.room_dict = dict_of_rooms
        self.unalloc_people = []

    def get_room_occupants(self, room_name):
        """ get the occupants of a specific room """
        return self.room_dict[room_name.lower()]

    def get_unallocated_people(self):
        return self.unalloc_people


class Office(Room):
    """ this class represents the office-space rooms """

    """ the capacity of a given office room """
    capacity = 6

    def populate_room_names(self):
        """ populate empty office space with room names """
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

    def unallocated_people(self, input_list):
        unalloc = []
        if len(input_list) > 0:
            for person in input_list:
                if person.has_office is False:
                    unalloc.append(person)
        return unalloc


class LivingSpace(Room):
    """ this class represents the living space for fellows """

    """ the capacity of a given office room """
    capacity = 4

    def populate_room_names(self):
        """ populate the empty living space  with room names """
        living = {
            'green': [], 'blue': [], 'yellow': [], 'lilac': [],
            'orange': [], 'white': [], 'brown': [],
            'turquoise': [], 'grey': [], 'purple': []
        }
        self.room_dict = dict([(key, []) for key in living])
        return self.room_dict

    def save(self, room_dictionary):
        """ Save allocated rooms with occupants """
        self.room_dict = room_dictionary
        return self.room_dict

    def unallocated_people(self, input_list):
        unalloc = []
        if len(input_list) > 0:
            for person in input_list:
                if person.has_living_space is False:
                    unalloc.append(person)
        return unalloc
