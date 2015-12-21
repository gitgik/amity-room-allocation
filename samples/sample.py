import os
import sys
import inspect
currentdir = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
from amity import Amity

amity = Amity()
amity.allocate_living_space(sys.argv[1], is_a_file=True)
amity.allocate_office_space(sys.argv[1], is_a_file=True)

amity.get_allocations()
amity.print_allocations()
