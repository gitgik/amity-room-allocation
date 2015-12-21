# !/usr/bin/python
import unittest
import nose

from employees.model import Person
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


class AllocationTestCase(unittest.TestCase):
    """ tests the allocation of rooms to persons """

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
        self.assertFalse(living_room.is_occupied())
        self.assertFalse(office_room.is_occupied())
        self.office = Office('GreenHouse')
        self.living = LivingSpace('BlueMoon')
        self.amity = Amity()

        ospace = self.amity.allocate_office_space(self.fellow)
        lspace = self.amity.allocate_living_space(self.fellow)
        allocated = self.office.get_occupants()
        self.assertEquals(self.staff.has_living_space(), False)
        self.assertEquals(self.fellow.has_living_space(), True)
        self.assertIsNotNone(allocated)
        self.assertIsNotNone(ospace)
        self.assertIsNotNone(lspace)

    def test_getting_room_occupants(self):
        """ tests getting a given room's occupants """
        self.amity = Amity()
        office_results = self.amity.allocate_office_space(
            file_path, is_a_file=True)
        living_results = self.amity.allocate_living_space(
            file_path, is_a_file=True)
        office_roomies = office_results[0].get_occupants()
        living_roomies = living_results[0].get_occupants()
        self.assertIsNotNone(office_roomies)
        self.assertIsNotNone(living_roomies)

    def test_getting_all_allocations(self):
        """ tests getting all allocations to the building """
        self.amity = Amity()
        self.amity.allocate_living_space(file_path, is_a_file=True)
        self.amity.allocate_office_space(file_path, is_a_file=True)
        allocations = self.amity.get_allocations()
        self.assertIsNotNone(allocations)

    def test_unallocated(self):
        """ test getting unallocated people if any """
        amity = Amity()
        amity.allocate_office_space(file_path, is_a_file=True)
        unalloc = amity.get_unallocated()
        # the rooms are currently 10, each taking 4 occupants,
        # therefore we don't have unallocated persons
        self.assertEquals(unalloc, [])



if __name__ == '__main__':
    nose.run()
