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
import re

# a list of living space
livings = [
    'green', 'blue', 'yellow', 'lilac',
    'orange', 'white', 'brown',
    'turquoise', 'grey', 'purple'
]

# a list of offices
offices = [
    "allegro", "boma", "valhalla",
    "hogwarts", "krypton", "oculus",
    "gondolla", "amitoid", "punta", "borabora"
]


class Amity(object):
    """ this class randomly allocates rooms to persons """

    def __init__(self):
        self.allocations = []
        self.unallocated = []

    def add_rooms(self, room_list, room_type):
        """ Instantiate offices and store them in a list """
        if room_type.lower() == 'office':
            room_list = [Office(room_name) for room_name in room_list]
        elif room_type.lower() == 'living':
            room_list = [LivingSpace(room_name) for room_name in room_list]
        return room_list

    def get_allocations(self):
        return self.allocations

    def print_allocations(self):
        """ Print all allocations """
        for room in self.allocations:
            print ("%s (%s)" % (room.name, room.room_type))
            for occupant in room.occupants:
                print (occupant.name)
            print ("\n")
        return True

    def get_unallocated(self):
        return self.unallocated

    @staticmethod
    def get_people_from_file(people_file):
        """ Parse from text file """
        people = []
        # read each line from the file and store in a temp list
        for line in open(people_file, 'r'):
            employee = line.rstrip('\n')
            match = re.search(
                '^(\w+\s[^\s]+)[\s]{1,}(\w+)[\s]{0,}(\w)?', employee)
            details = match.groups()
            name, role, wants_accomodation = details
            # create the person with the credentials
            person = Person.create(name, role, wants_accomodation)
            people.append(person)

        # randomly shuffle the employee list
        # to prevent unrandom FIFO behavior every time we re-allocate rooms
        random.shuffle(people)

        return people

    def allocate_office_space(self, input_file, is_a_file=False):
        """ Allocate office space """
        # add room names to the office list
        offices_list = self.add_rooms(offices, 'office')

        # shuffle room numbers at random
        # use list() to support python 3
        room_index = list(range(10))
        random.shuffle(room_index)
        # read each line of input .txt file
        if is_a_file is True:
            employees = self.get_people_from_file(input_file)
        else:
            employees = []
            employees.append(input_file)

        index = 0

        # loop through each person to determine their affiliations
        for person in employees:
            if isinstance(person, Staff) or isinstance(person, Fellow):
                chosen_room_index = room_index[index % 10]
                chosen_office = offices_list[chosen_room_index]
                # check whether the room has space for an allocation
                if not chosen_office.is_occupied():
                    # allocate office space to everyone
                    person.assign_office_space(chosen_office)
                    chosen_office.assign_person(person)
                    self.allocations.append(chosen_office)
                else:
                    self.unallocated.append(person)
                index += 1

        return offices_list

    def allocate_living_space(self, input_file, is_a_file=False):
        """ allocate living space """
        # add rooms to the living lists
        livings_list = self.add_rooms(livings, 'living')

        # shuffle room numbers at random
        # use list() to support python 3
        room_index = list(range(10))
        random.shuffle(room_index)
        # read each line of input .txt file
        if is_a_file is True:
            employees = self.get_people_from_file(input_file)
        else:
            employees = []
            employees.append(input_file)

        index = 0

        # loop through each person to determine their affiliations
        for person in employees:
            # ensure the rooms are available
            if isinstance(person, Fellow):
                if person.wants_living_space():
                    chosen_room_index = room_index[index % 10]
                    chosen_living_room = livings_list[chosen_room_index]
                    # check whether the room has space for an allocation
                    if not chosen_living_room.is_occupied():
                        # a fellow needs a place to live too
                        person.assign_living_space(chosen_living_room)
                        chosen_living_room.assign_person(person)
                        self.allocations.append(chosen_living_room)
                    else:
                        self.unallocated.append(person)
                    index += 1

        return livings_list
