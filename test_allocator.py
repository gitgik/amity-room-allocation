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

import unittest
import nose

from random import randint
from employees.model import Person, Fellow, Staff
from rooms.models import LivingSpace, Office
from amity import Amity

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
# instantiate offices and store them in a list
offices_list = [Office(office_name) for office_name in office_spaces]


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
        # create rooms and test against their class instances
        self.office = Office('Valhalla')
        self.living = LivingSpace('PeckingOrder')
        self.assertIsInstance(self.office, Office)
        self.assertIsInstance(self.living, LivingSpace)

    def test_person_creation(self):
        # create employees and test against their class instances
        self.fellow = Person.create(
            'Jee Gikera', 'fellow', wants_accomodation=True)
        self.staff = Person.create('Chidi Nnadi', 'staff')
        self.assertIsInstance(self.fellow, Fellow)
        self.assertIsInstance(self.staff, Staff)


class AllocationTestCase(unittest.TestCase):
    """ tests the allocation of rooms to persons """

    def test_room_generation(self):
        # generate rooms and test their specs
        self.office = Office('TopOffice')
        self.living = LivingSpace('WoodWing')
        office_size = self.office.capacity
        living_size = self.living.capacity
        self.assertEquals(office_size, 6)
        self.assertEquals(living_size, 4)

    def test_allocation_to_rooms(self):
        # tests the allocation of persons to rooms
        self.fellow = Person.create(
            'Jee Gikera', 'fellow', wants_accomodation='Y')
        self.staff = Person.create('Chidi Nnadi', 'staff')
        office_room = Office('valhalla')
        living_room = LivingSpace('blue')
        # store person instances for testing
        fellow_only.append(self.fellow)
        persons.append(self.staff)
        persons.append(self.fellow)

        office_results = self.staff.assign_office_space(office_room)
        living_results = self.fellow.assign_living_space(living_room)
        office_room.assign_person(self.staff)
        living_room.assign_person(self.fellow)
        self.assertTrue(self.staff.has_office())
        self.assertTrue(self.fellow.has_living_space())
        self.assertIsInstance(office_results, Office)
        self.assertIsInstance(living_results, LivingSpace)
        self.assertIsNotNone(living_room)
        self.assertIsNotNone(office_room)
        self.assertTrue(living_room.is_occupied())
        self.assertTrue(office_room.is_occupied())
        self.office = Office('GreenHouse')
        self.living = LivingSpace('BlueMoon')
        self.amity = Amity()

        ospace = self.amity.allocate_office_space(offices_list, self.fellow)
        lspace = self.amity.allocate_living_space(offices_list, self.fellow)
        allocated = self.office.get_occupants()
        self.assertEquals(self.staff.has_living_space(), False)
        self.assertEquals(self.fellow.has_living_space(), True)
        self.assertIsNotNone(allocated)
        self.assertIsNotNone(ospace)
        self.assertIsNotNone(lspace)

    def test_finding_room_occupants(self):
        """ tests getting a given room's occupants """
        self.amity = Amity()
        office_results = self.amity.allocate_office_space(
            offices_list, file_path, is_a_file=True)
        living_results = self.amity.allocate_living_space(
            livings_list, file_path, is_a_file=True)
        office_roomies = office_results[0].get_occupants()
        living_roomies = living_results[0].get_occupants()
        self.assertIsNotNone(office_roomies)
        self.assertIsNotNone(living_roomies)


class FileInputTestCase(unittest.TestCase):
    """ tests file IO to the program """

    def test_parsing_file(self):
        persons = Amity.get_people_from_file(file_path)
        self.assertEquals(len(persons), 43)
        self.assertIsInstance(persons[randint(0, 30)], Person)

if __name__ == '__main__':
    nose.run()
