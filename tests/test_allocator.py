import unittest
import nose

from random import randint
from employees.model import Person, Fellow, Staff
from rooms.models import LivingSpace, Office
from amity import Amity

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
        self.assertIsInstance(self.office, Office)
        self.assertIsInstance(self.living_space, LivingSpace)

    def test_fellow_staff_creation(self):
        self.assertIsInstance(self.f, Fellow)
        self.assertIsInstance(self.staff, Staff)


class FileInputTestCase(unittest.TestCase):
    def test_can_parse_people_from_file(self):
        persons = Amity.get_people_from_file(file_path)
        self.assertEquals(len(persons), 43)
        self.assertIsInstance(persons[randint(0, 30)], Person)

if __name__ == '__main__':
    nose.run()
