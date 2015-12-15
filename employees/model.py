# models.py
class Person(object):
    def __init__(self, name):
        self.name = name

    def has_office(self):
        """ check if person has been assigned a room """
        return True if self.office is not None else False

    def assign_office(self, office):
        """ assign a person to an office provided """
        self.office = office


class Staff(Person):
    """ represents a staff in amity"""
    def has_living_space(self):
        return False


class Fellow(Person):
    """ represents a fellow in amity """
    def wants_living_space(self):
        return True if self.wants_accomodation else False

    def has_living_space(self):
        """ check if a fellow has accomodation """
        return True if self.living_space is not None else False

    def assign_living_space(self, room):
        """ assign accomodation room to fellow """
        self.living_space = room

    def __init__(self, name, is_living):
        self.is_living = is_living
        super(Fellow, self).__init__(name)
