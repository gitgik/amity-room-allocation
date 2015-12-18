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


class Person(object):
    """ this class represents a person """

    def __init__(self, name):
        self.name = name

    @staticmethod
    def create(name, role, wants_accomodation=False):
        """ create an instance of a fellow or a staff person """
        a_person = Role.type_of[role.lower()]
        person = a_person(name)
        person.office = None
        if isinstance(person, Staff):
            person.wants_accomodation = False
        if isinstance(person, Fellow):
            if wants_accomodation == 'Y' or wants_accomodation is True:
                person.wants_accomodation = True
            else:
                person.wants_accomodation = False
            person.living_space = None
        return person

    def has_office(self):
        """ check if person has been assigned a room """
        return True if self.office is not None else False

    def assign_office(self, office):
        """ assign a person to an office provided """
        self.office = office
        return self.office

    def __repr__(self):
        return "(Fellow: {0}, {1})".format(self.name, self.wants_accomodation)


class Staff(Person):
    """ this class represents a staff in amity """

    def has_living_space(self):
        return False

    def __repr__(self):
        return "(Staff: {0}, {1})".format(self.name, self.wants_accomodation)


class Fellow(Person):
    """ this class represents a fellow in amity """

    def wants_living_space(self):
        return True if self.wants_accomodation else False

    def assign_living_space(self, room):
        """ assign accomodation room to fellow """
        self.living_space = room
        return self.living_space

    def has_living_space(self):
        """ check if a fellow has accomodation """
        return True if self.wants_accomodation is True else False

    def __repr__(self):
        return "(Fellow: {0}, {1})".format(self.name, self.wants_accomodation)


class Role:
    """
        this class represents the collective role of a person:
        either fellow or staff
    """
    type_of = {'fellow': Fellow, 'staff': Staff}
