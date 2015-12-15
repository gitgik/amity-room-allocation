import unittest
from rooms.models import Room, LivingSpace, Office



class Tdd(unittest.TestCase):
    def test_Office_maximum_size_returns_correct_result(self):
        rooms = []
        office = Office(rooms)
        result = office.maximum_size
        self.assertEqual(6, result)

if __name__ == '__main__':
    unittest.main()