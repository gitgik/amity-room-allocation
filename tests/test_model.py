# !/usr/bin/python
import unittest
from employees.model import Person, Fellow, Staff
from rooms.models import LivingSpace, Office

# file path to the input .txt file containing people
file_path = 'input.txt'
persons = []
fellow_only = []

# a list of living space
living_spaces = [
    'green', 'blue', 'yellow', 'lilac',
    'orange', 'white', 'brown',
    'turquoise', 'grey', 'purple'
]
# create the office list
livings_list = [
    LivingSpace(living_space_name)
    for living_space_name in living_spaces
]

# a list of offices
office_spaces = [
    "allegro", "boma", "valhalla",
    "hogwarts", "krypton", "oculus",
    "gondolla", "amitoid", "punta", "borabora"
]


class RoomPersonTestCase(unittest.TestCase):
    """ test the instantiation of rooms and people """

    def setup(self):
        self.office = Office()
        self.living = LivingSpace()
        self.office.populate_room_names()
        self.living.populate_room_names()
        self.f = Person.create(
            'Jee Gikera', 'fellow', wants_accomodation=True)
        self.staff = Person.create('Chidi Nnadi', 'staff')

    def test_room_creation(self):
        # generate rooms and test their specs
        self.office = Office('TopOffice')
        self.living = LivingSpace('WoodWing')
        office_size = self.office.capacity
        living_size = self.living.capacity
        self.assertEquals(office_size, 6)
        self.assertEquals(living_size, 4)
        self.assertIsInstance(self.office, Office)
        self.assertIsInstance(self.living, LivingSpace)

    def test_person_creation(self):
        # create employees and test against their class instances
        self.fellow = Person.create(
            'Jee Gikera', 'fellow', wants_accomodation=True)
        self.staff = Person.create('Chidi Nnadi', 'staff')
        self.assertIsInstance(self.fellow, Fellow)
        self.assertIsInstance(self.staff, Staff)
