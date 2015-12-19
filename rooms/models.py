# !/usr/bin/python
# title          :amity/alloc.py
# description    :An algorithm which randomly allocates
#                 persons to rooms in a building.
# author         :Jee Githinji
# email          :githinji.gikera@andela.com
# date           :12-18-2015
# version        :0.0.1
# python_version :2.7.10
# ==============================================================================

from employees.model import Staff, Fellow


class Room(object):
    """ this class represents a room in a building """

    def __init__(self, name):
        self.name = name


class Office(Room):
    """ this class represents the office-space rooms """
    def __init__(self, name):
        self.capacity = 6
        self.occupants = []

    def is_occupied(self):
        return len(self.occupants) < self.capacity

    def assign_person(self, person):
        if self.capacity >= len(self.occupants):
            if isinstance(person, Staff) or isinstance(person, Fellow):
                self.occupants.append(person)
        return self.occupants

    def get_occupants(self):
            return self.occupants

    def unallocated_people(self, input_list):
        unalloc = []
        if len(input_list) > 0:
            for person in input_list:
                if person.has_office is False:
                    unalloc.append(person)
        return unalloc

    def __repr__(self):
        return "Office: {0}".format(self.name)


class LivingSpace(Room):
    """ this class represents the living space for fellows """

    # the capacity of a given office room
    capacity = 4
    occupants = []

    def is_occupied(self):
        return len(self.occupants) < self.capacity

    def assign_person(self, person):
        if self.capacity >= len(self.occupants):
            if isinstance(person, Staff) or isinstance(person, Fellow):
                self.occupants.append(person)
        return False

    def get_occupants(self):
            return self.occupants

    def unallocated_people(self, input_list):
        unalloc = []
        if len(input_list) > 0:
            for person in input_list:
                if person.has_living_space is False:
                    unalloc.append(person)
        return unalloc

    def __repr__(self):
        return "LivingSpace: {0}".format(self.name)
