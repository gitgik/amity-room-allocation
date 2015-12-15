# amity.py
from employees.model import Person
from rooms.models import Office, LivingSpace
import random
import sys

""" exit gracefully when the text file to read is missing """
if __name__ == "__main__":
    try:
        arg1 = sys.argv[1]
    except IndexError:
        print "Usage: myprogram.py <text file>"
        sys.exit(1)


""" office names: will contain names of people after allocations """
office = {
    "allegro": [], "boma": [], "valhalla": [],
    "hogwarts": [], "krypton": [], "oculus": [],
    "gondolla": [], "amitoid": [], "punta": [], "borabora": []
}

""" living space names """
living = {
    'Green': [], 'Blue': [], 'Yellow': [], 'Lilac': [],
    'Orange': [], 'White': [], 'Brown': [],
    'Turquoise': [], 'Grey': [], 'Purple': []
}
""" create a list of rooms (both office and living space)
    which will be used to obtain the key to their respective
    dictionary definitions during allocations
"""
office_list = [
    'allegro', 'boma', 'valhalla',
    'hogwarts', 'krypton', 'oculus', 'gondolla',
    'amitoid', 'punta', 'borabora'
]

livingspace_list = [
    'Green', 'Blue', 'Yellow', 'Lilac',
    'Orange', 'White', 'Brown', 'Turquoise', 'Grey', 'Purple'
 ]


class Amity(object):
    """ get the occupants in a given room"""
    def get_room_occupants(self, room_name):
        o = self.allocate_office_space()
        l = self.allocate_living_space()
        return o[room_name] or l[room_name]

    """ allocate office space """
    def allocate_office_space(self):
        listof = Person()
        unallocated = listof.unallocated()

        office_space = Office(office)
        office_rooms = office_space.populate_room_names()

        """ shuffle room numbers at random """
        room_index = list(range(10))
        random.shuffle(room_index)

        """ read each line of input .txt file """
        employees = [
            employees.rstrip('\n') for employees in open(sys.argv[1], 'r')
        ]

        """ randomly shuffle the employee list
           to prevent FIFO repetition  every time we allocate rooms """
        random.shuffle(employees)

        index = 0

        """ loop through each person to determine their affiliations """
        for person in employees:
            """ use space char as the delimeter """
            persons_description = [x.rstrip() for x in person.split(' ')]

            chosen_room = room_index[index % 10]
            office_key = office_list[chosen_room]

            """ allocate only office space if space is available """
            if len(office_rooms[office_key]) < office_space.maximum_size:
                """ allocate office space to everyone """
                office_rooms[office_key].append(
                    persons_description[0] + ' ' + persons_description[1])
            else:
                """ those who missed rooms """
                unallocated.append(
                    persons_description[0] + ' ' + persons_description[1])

            """ pick a different room for the next iteration """
            index += 1

        return office_rooms

    """ allocate living space """
    def allocate_living_space(self):
        unallocated_people = []
        living_space = LivingSpace(living)
        living_rooms = living_space.populate_room_names()

        """ shuffle room numbers at random """
        room_index = list(range(10))
        random.shuffle(room_index)
        print room_index

        """ read the employees from the input .txt file """
        employees = [
            employees.rstrip('\n') for employees in open(sys.argv[1], 'r')
        ]
        living_fellows = []
        person_traits = []
        for person in employees:
            person_traits = person.split(' ')
            if len(person_traits) == 4:
                if person_traits[3].upper() == 'Y':
                    living_fellows.append(person)

        """ randomly shuffle the employee list
           to prevent FIFO repetition  every time we allocate rooms """
        random.shuffle(living_fellows)

        index = 0
        """ loop through each person to determine their affiliations """
        for person in living_fellows:
            """ use space char as the delimeter """
            persons_description = [x.rstrip() for x in person.split(' ')]

            chosen_room = room_index[index % 10]
            living_key = livingspace_list[chosen_room]
            """ ensure the rooms are available """
            if len(living_rooms[living_key]) < living_space.maximum_size:
                """ a fellow needs a place to live too """
                living_rooms[living_key].append(
                    persons_description[0] +
                    ' ' + persons_description[1])
            else:
                """ those who missed rooms """
                unallocated_people.append(
                    persons_description[0] + ' ' + persons_description[1])
            index += 1

        return living_rooms

amity = Amity()
print amity.allocate_office_space()
print amity.allocate_living_space()
