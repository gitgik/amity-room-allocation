import unittest
from rooms.models import LivingSpace, Office
from amity import Amity


class TestAllocator(unittest.TestCase):
    def test_command_line_argument_missing(self):
        pass

    def test_room_allocations_returns_not_empty(self):
        amity = Amity()
        office = Office()
        living_space = LivingSpace()
        empty_office_space = office.populate_room_names()
        empty_living_space = living_space.populate_room_names()

        office.save(amity.allocate_office_space())
        living_space.save(amity.allocate_living_space())

        self.assertNotEqual(empty_office_space, office.room_dict)
        self.assertNotEqual(empty_living_space, living_space.room_dict)

if __name__ == '__main__':
    unittest.main()