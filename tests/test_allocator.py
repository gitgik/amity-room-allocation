import unittest
import nose

from random import randint
from employees.model import Person, Fellow, Staff
from rooms.models import LivingSpace, Office
from amity import Amity
""" file path to the input .txt file containing people """
file_path = 'input.txt'


class RoomPersonTestCase(unittest.TestCase):
    def setup(self):
        self.office = Office()
        self.living = LivingSpace()
        self.office.populate_room_names()
        self.living.populate_room_names()
        self.f = Person.create(
            'Jee Gikera', 'fellow', wants_accomodation=True)
        self.staff = Person.create('Chidi Nnadi', 'staff')

    def test_room_creation(self):
        self.office = Office()
        self.living = LivingSpace()
        self.assertIsInstance(self.office, Office)
        self.assertIsInstance(self.living, LivingSpace)

    def test_fellow_staff_creation(self):
        self.f = Person.create(
            'Jee Gikera', 'fellow', wants_accomodation=True)
        self.staff = Person.create('Chidi Nnadi', 'staff')
        self.assertIsInstance(self.f, Fellow)
        self.assertIsInstance(self.staff, Staff)


class AllocationTestCase(unittest.TestCase):
        def test_room_generation(self):
            self.office = Office()
            self.living = LivingSpace()
            office_rooms = self.office.populate_room_names()
            living_rooms = self.living.populate_room_names()
            self.assertEquals(len(office_rooms), 10)
            self.assertEquals(len(living_rooms), 10)

        def test_allocation_to_rooms(self):
            self.office = Office()
            self.living = LivingSpace()
            self.amity = Amity()
            o = self.office.save(self.amity.allocate_office_space(file_path))
            l = self.living.save(self.amity.allocate_living_space(file_path))

            self.assertIsNotNone(o)
            self.assertIsNotNone(l)

        def test_finding_room_occupants(self):
            self.office = Office()
            self.living = LivingSpace()
            self.amity = Amity()
            self.office.save(self.amity.allocate_office_space(file_path))
            self.living.save(self.amity.allocate_living_space(file_path))
            valhalla_roomies = self.office.get_room_occupants('valhalla')
            green_roomies = self.living.get_room_occupants('green')
            assigned_person1 = valhalla_roomies[0]
            assigned_person2 = green_roomies[0]
            self.assertIsInstance(assigned_person1, Person)
            self.assertIsInstance(assigned_person2, Person)


class FileInputTestCase(unittest.TestCase):
    def test_can_parse_people_from_file(self):
        persons = Amity.get_people_from_file(file_path)
        self.assertEquals(len(persons), 43)
        self.assertIsInstance(persons[randint(0, 30)], Person)

if __name__ == '__main__':
    nose.run()
