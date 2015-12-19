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
import re

# exit gracefully when the text file to read is missing
if __name__ == "__main__":
    try:
        arg1 = sys.argv[1]
    except IndexError:
        print ("Usage: python amity.py <text file>")
        sys.exit(1)

# a list of living space
livings = [
    'green', 'blue', 'yellow', 'lilac',
    'orange', 'white', 'brown',
    'turquoise', 'grey', 'purple'
]
# create the office list
livings_list = [
    LivingSpace(living_space_name)
    for living_space_name in livings
]

# a list of offices
offices = [
    "allegro", "boma", "valhalla",
    "hogwarts", "krypton", "oculus",
    "gondolla", "amitoid", "punta", "borabora"
]
# instantiate offices and store them in a list
offices_list = [Office(office_name) for office_name in offices]


class Amity(object):
    """ this class randomly allocates rooms to persons """

    @staticmethod
    def get_people_from_file(people_file):
        """ parse from text file """

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

    def allocate_office_space(self, offices_list, input_file, is_a_file=False):
        """ allocate office space """

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
            index += 1

        return offices_list

    def allocate_living_space(self, livings_list, input_file, is_a_file=False):
        """ allocate living space """

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
            index += 1

        return livings_list

# amity = Amity()
# l = amity.allocate_living_space(sys.argv[1], is_a_file=True)
# o = amity.allocate_office_space(sys.argv[1], is_a_file=True)
# for i in l:
#     print i.occupants
# print '\n'
# for i in o:
#     print i.occupants
