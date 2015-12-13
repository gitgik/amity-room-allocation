# amity.py
from employees.model import Staff, Fellow
from rooms.models import Office, LivingSpace
import random
import sys

""" office names: will contain names of people after allocations """
allegro, boma, valhalla, hogwarts = [], [], [], []
krypton, oculus, gondolla = [], [], []
amitoid, punta, borabora = [], [], []

office_rooms = [
    allegro, boma, valhalla, hogwarts, krypton, oculus,
    gondolla, amitoid, punta, borabora]

""" living space names """
Green, Blue, Yellow, Lilac = [], [], [], []
Orange, White, Brown, Turquoise, Grey, Purple = [], [], [], [], [], []

living_rooms = [
    Green, Blue, Yellow, Lilac,
    Orange, White, Brown, Turquoise, Grey, Purple
]


class Amity(object):
    def print_rooms(self):
        office = Office(office_rooms)
        print office.populate_room_names()

    def allocate_room(self):
        office = Office(office_rooms)
        office_names = office.populate_room_names()
        """ shuffle room numbers at random """
        room_index = list(range(len(office_names)))
        random.shuffle(room_index)
        print room_index

        """ read the employees from the input .txt file """
        employees = [
            employees.rstrip('\n') for employees in open(sys.argv[1], 'r')
        ]

        """ loop through each person to determine their affiliations """
        for i in employees:
            persons_description = [x.rstrip() for x in i.split(" ")]
            """ allocate to a random office """
            for random_room in room_index:
                """ check whether they are fellows or employees """
                if persons_description[2] == "Staff":
                    """ allocate only office space """
                    office_names[random_room].append(
                        persons_description[0] + ' ' + persons_description[1])
                    print office_names[random_room]
                else:
                    pass
                    # maximum = office.maximum_size
                    # rand = round(random.random() * maximum)

amity = Amity()
amity.print_rooms()
amity.allocate_room()

