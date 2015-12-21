# file io test
import unittest
import nose
import random
from employees.model import Person
from amity import Amity

# file path to the input .txt file containing people
file_path = 'input.txt'
persons = []


class FileInputTestCase(unittest.TestCase):
    """ tests file IO to the program """

    def test_parsing_file(self):
        persons = Amity.get_people_from_file(file_path)
        self.assertEquals(len(persons), 62)
        self.assertIsInstance(persons[random.randint(0, 30)], Person)

if __name__ == '__main__':
    nose.run()
