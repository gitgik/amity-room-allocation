# models.py
class Person(object):
    def __init__(self):
        pass

    def unallocated(self):
        return list()


class Staff(Person):
    pass


class Fellow(Person):
    def __init__(self, name, is_living):
        self.is_living = is_living
        super(Fellow, self).__init__(name)
