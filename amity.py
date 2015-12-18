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

from employees.model import Person, Fellow, Staff
from rooms.models import Office, LivingSpace
import random
import sys
from re import search

""" exit gracefully when the text file to read is missing """
if __name__ == "__main__":
    try:
        arg1 = sys.argv[1]
    except IndexError:
        print ("Usage: python amity.py <text file>")
        sys.exit(1)

"""
    create a list of keys to the office
    dictionary definitions during random allocations
"""
office_list = [
    'allegro', 'boma', 'valhalla',
    'hogwarts', 'krypton', 'oculus', 'gondolla',
    'amitoid', 'punta', 'borabora'
]
"""
    create a list of keys to the living space
    dictionary definitions during random allocations
"""
livingspace_list = [
    'green', 'blue', 'yellow', 'lilac',
    'orange', 'white', 'brown', 'turquoise', 'grey', 'purple'
]


class Amity(object):
    """ this class randomly allocates rooms to persons """

    @staticmethod
    def get_people_from_file(people_file):
        """ parse from text file """

        people = list()
        """ read each line from the file and store in a temp list """
        employees = [
            employees.rstrip('\n') for employees in open(people_file, 'r')
        ]
        for line in employees:
            match = search(
                '^(\w+\s[^\s]+)[\s]{1,}(\w+)[\s]{0,}(\w)?', line)
            details = match.groups()
            name, role, wants_accomodation = details
            """ create the person with the credentials """
            person = Person.create(name, role, wants_accomodation)
            people.append(person)

        """
        randomly shuffle the employee list
        to prevent unrandom FIFO behavior every time we re-allocate rooms
        """
        random.shuffle(people)
        return people

    def allocate_office_space(self, input_file, is_a_file=False):
        """ allocate office space """
        office_space = Office()
        office_rooms = office_space.populate_room_names()
        unalloc = []

        """ shuffle room numbers at random """
        room_index = list(range(10))
        random.shuffle(room_index)

        """ read each line of input .txt file """
        if is_a_file is True:
            employees = self.get_people_from_file(input_file)
        else:
            employees = []
            employees.append(input_file)

        index = 0

        """ loop through each person to determine their affiliations """
        for person in employees:
            if isinstance(person, Staff) or isinstance(person, Fellow):
                chosen_room = room_index[index % 10]
                office_key = office_list[chosen_room]

                """ check whether the room has space for an allocation """
                if len(office_rooms[office_key]) < office_space.capacity:
                    """ allocate office space to everyone """
                    person.assign_office(office_key)
                    office_rooms[office_key].append(person)
                else:
                    """ those who missed rooms """
                    unalloc.append(person)

            """ pick a different room for the next iteration """
            index += 1
        if len(unalloc) > 0:
            office_space.unallocated_people(unalloc)

        return office_rooms

    """ allocate living space """
    def allocate_living_space(self, input_file, is_a_file=False):
        living_space = LivingSpace()
        living_rooms = living_space.populate_room_names()
        unalloc = []

        """ shuffle room numbers at random """
        room_index = list(range(10))
        random.shuffle(room_index)

        """ read each line of input .txt file """
        if is_a_file is True:
            employees = self.get_people_from_file(input_file)
        else:
            employees = []
            employees.append(input_file)

        index = 0
        """ loop through each person to determine their affiliations """
        for person in employees:
            """ ensure the rooms are available """
            if isinstance(person, Fellow):
                chosen_room = room_index[index % 10]
                living_key = livingspace_list[chosen_room]

                """ check whether the room has space for an allocation """
                if len(living_rooms[living_key]) < living_space.capacity:
                    """ a fellow needs a place to live too """
                    if person.wants_living_space():
                        person.assign_living_space(living_key)
                        living_rooms[living_key].append(person)
                else:
                    """ those who missed rooms """
                    unalloc.append(person)
            index += 1
        if len(unalloc) != 0:
            living_space.unallocated_people(unalloc)
        return living_rooms
