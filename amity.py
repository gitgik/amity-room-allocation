# amity.py
from employees.model import Staff, Fellow
from rooms.models import Office, LivingSpace
import random
import sys

""" office names: will contain names of people after allocations """
office_rooms = {
    "allegro": [], "boma": [], "valhalla": [],
    "hogwarts": [], "krypton": [], "oculus": [],
    "gondolla": [], "amitoid": [], "punta": [], "borabora": []
}

""" living space names """
living_rooms = {
    'Green': [], 'Blue': [], 'Yellow': [], 'Lilac': [],
    'Orange': [], 'White': [], 'Brown': [],
    'Turquoise': [], 'Grey': [], 'Purple': []
}
""" create a list of rooms (both office and living space)
    which will be used to obtain the key to their respective
    dictionary definitions during allocations
"""
office_list = [
    'allegro', 'boma', 'valhalla',
    'hogwarts', 'krypton', 'oculus', 'gondolla',
    'amitoid', 'punta', 'borabora'
]

livingspace_list = [
    'Green', 'Blue', 'Yellow', 'Lilac',
    'Orange', 'White', 'Brown', 'Turquoise', 'Grey', 'Purple'
 ]

class Amity(object):
    def print_rooms(self):
        office = Office(office_rooms)
        print office.populate_room_names()

    def allocate_room(self):
        office = Office(office_rooms)
        office_names = office.populate_room_names()
        livingspace = LivingSpace(living_rooms)
        living_names = livingspace.populate_room_names()

        """ shuffle room numbers at random """
        room_index = list(range(len(office_names)))
        random.shuffle(room_index)
        print room_index

        """ read the employees from the input .txt file """
        employees = [
            employees.rstrip('\n') for employees in open(sys.argv[1], 'r')
        ]
        index = 0
        """ loop through each person to determine their affiliations """
        for i in employees:
                chosen_room = room_index[index]
                persons_description = [x.rstrip() for x in i.split(" ")]

                """ check whether they are fellows or employees """
                if persons_description[2] == "Staff":
                    """ allocate only office space """
                    key = office_list[chosen_room]
                    office_names[key].append(
                        persons_description[0] + ' ' + persons_description[1])
                elif persons_description[2] == "Fellow":
                    okey = office_list[chosen_room]
                    lkey = livingspace_list[chosen_room]
                    if len(persons_description) >= 4:
                        """ fellow needs a place to live AND office """
                        office_names[okey].append(
                            persons_description[0] +
                            ' ' + persons_description[1])
                        living_names[lkey].append(
                            persons_description[0] +
                            ' ' + persons_description[1])
                    else:
                        """ fellow does not need accomodation """
                        office_names[okey].append(
                            persons_description[0] +
                            ' ' + persons_description[1])


                index += 1
                        # maximum = office.maximum_size
                        # rand = round(random.random() * maximum)

        print office_names
amity = Amity()
amity.print_rooms()
amity.allocate_room()

