# amity.py
from employees.model import Staff, Fellow
from rooms.models import Office, LivingSpace
import random
import sys

office_rooms = [
    'Orange', 'Lilac', 'Valhalla', 'Hogwarts', 'Krypton', 'Oculus',
    'Gondolla', 'Amitoid', 'Punta', 'Borabora']
living_rooms = [
    'Green', 'Blue', 'Yellow', 'Lilac',
    'Orange', 'White', 'Brown', 'Turquoise', 'Grey', 'Purple'
]


class Amity(object):
    def print_rooms(self):
        office = Office(office_rooms)
        print office.pre_populate()

    def allocate_room(self):
        """ read the employees from the input .txt file """
        employees = [
            employees.rstrip('\n') for employees in open(sys.argv[1], 'r')
        ]

        office = Office(office_rooms)
        maximum = office.maximum_size
        rand = round(random.random() * maximum)
        print rand
        print employees

amity = Amity()
amity.print_rooms()
amity.allocate_room()

