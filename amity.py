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
        living = LivingSpace(living_rooms)
        office_names = office.populate_room_names()
        livingspace = LivingSpace(living_rooms)
        living_names = livingspace.populate_room_names()

        """ shuffle room numbers at random """
        room_index = list(range(10))
        random.shuffle(room_index)
        print room_index

        """ read the employees from the input .txt file """
        employees = [
            employees.rstrip('\n') for employees in open(sys.argv[1], 'r')
        ]
        index = 0
        """ loop through each person to determine their affiliations """
        for person in employees:
            """ use space char as the delimeter """
            persons_description = [x.rstrip() for x in person.split(" ")]

            chosen_room = room_index[index % 10]
            living_key = livingspace_list[chosen_room]
            office_key = office_list[chosen_room]

            if len(office_names[office_key]) <= office.maximum_size:
                """ check whether they are fellows or staff """
                if persons_description[2].upper() == 'STAFF' or 'FELLOW':
                    """ allocate only office space """
                    office_names[office_key].append(
                        persons_description[0] + ' ' + persons_description[1])

            if len(living_names[living_key]) <= living.maximum_size:
                if persons_description[2].upper() == 'FELLOW':
                    if len(persons_description) >= 4:
                        if persons_description[3] == 'Y':
                            """ fellow needs a place to live too """
                            living_names[living_key].append(
                                persons_description[0] +
                                ' ' + persons_description[1])

            """ pick a different room next iteration """
            index += 1

        print office_names
        print living_names
amity = Amity()
amity.allocate_room()

