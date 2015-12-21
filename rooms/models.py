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
        self.occupants = []

    def get_occupants(self):
            return self.occupants


class Office(Room):
    """ this class represents the office-space rooms """
    capacity = 6
    room_type = "Office"

    def is_occupied(self):
        return len(self.occupants) == self.capacity

    def assign_person(self, person):
        if self.capacity > len(self.occupants):
            if isinstance(person, Staff) or isinstance(person, Fellow):
                self.occupants.append(person)
        return self.occupants


class LivingSpace(Room):
    """ this class represents the living space for fellows """

    # the capacity of a given office room
    capacity = 4
    room_type = "LivingSpace"

    def is_occupied(self):
        return len(self.occupants) == self.capacity

    def assign_person(self, person):
        if self.capacity > len(self.occupants):
            if isinstance(person, Fellow):
                self.occupants.append(person)
        return self.occupants
