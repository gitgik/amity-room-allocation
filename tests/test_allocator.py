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
""" file path to the input .txt file containing people """
file_path = 'input.txt'


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
        """ create rooms and test against their class instances """
        self.office = Office()
        self.living = LivingSpace()
        self.assertIsInstance(self.office, Office)
        self.assertIsInstance(self.living, LivingSpace)

    def test_fellow_staff_creation(self):
        """ create employees and test against their class instances """
        self.fellow = Person.create(
            'Jee Gikera', 'fellow', wants_accomodation=True)
        self.staff = Person.create('Chidi Nnadi', 'staff')
        self.assertIsInstance(self.fellow, Fellow)
        self.assertIsInstance(self.staff, Staff)


class AllocationTestCase(unittest.TestCase):
    """ tests the allocation of rooms to persons """

    def test_room_generation(self):
        """ generate rooms and test their specs """
        self.office = Office()
        self.living = LivingSpace()
        office_size = self.office.capacity
        living_size = self.living.capacity
        office_rooms = self.office.populate_room_names()
        living_rooms = self.living.populate_room_names()
        self.assertEquals(len(office_rooms), 10)
        self.assertEquals(len(living_rooms), 10)
        self.assertEquals(office_size, 6)
        self.assertEquals(living_size, 4)

    def test_allocation_to_rooms(self):
        """ tests the allocation of rooms """
        self.f = Person.create(
            'Jee Gikera', 'fellow', wants_accomodation='Y')
        self.s = Person.create('Chidi Nnadi', 'staff')
        self.office = Office()
        self.living = LivingSpace()
        self.a = Amity()
        fellows_l_space = self.living.save(
            self.a.allocate_office_space(self.f))
        self.office.save(
            self.a.allocate_office_space(self.s))
        unallocated = self.office.get_unallocated_people()
        self.assertEquals(self.s.has_living_space(), False)
        self.assertEquals(self.f.has_living_space(), True)
        self.assertEquals(self.s.has_office(), True)
        self.assertEquals(self.f.has_office(), True)
        self.assertListEqual(unallocated, [])
        self.assertIsNotNone(fellows_l_space)

    def test_finding_room_occupants(self):
        """ tests getting a given room's occupants """
        self.office = Office()
        self.living = LivingSpace()
        self.amity = Amity()
        self.office.save(
            self.amity.allocate_office_space(file_path, is_a_file=True))
        self.living.save(
            self.amity.allocate_living_space(file_path, is_a_file=True))
        valhalla_roomies = self.office.get_room_occupants('valhalla')
        blue_roomies = self.living.get_room_occupants('blue')
        assigned_person1 = valhalla_roomies[0]
        assigned_person2 = blue_roomies[0]
        self.assertIsInstance(assigned_person1, Person)
        self.assertIsInstance(assigned_person2, Person)


class FileInputTestCase(unittest.TestCase):
    """ tests file IO to the program """

    def test_can_parse_people_from_file(self):
        persons = Amity.get_people_from_file(file_path)
        self.assertEquals(len(persons), 43)
        self.assertIsInstance(persons[randint(0, 30)], Person)

if __name__ == '__main__':
    nose.run()
