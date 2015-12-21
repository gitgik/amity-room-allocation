import os
import sys
import inspect
currentdir = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from amity import Amity


# exit gracefully when the text file to read is missing
if __name__ == "__main__":
    try:
        arg1 = sys.argv[1]
    except IndexError:
        print ("Usage: python sample.py <text file>")
        sys.exit(1)

amity = Amity()
amity.allocate_living_space(sys.argv[1], is_a_file=True)
amity.allocate_office_space(sys.argv[1], is_a_file=True)

amity.get_allocations()
amity.print_allocations()
amity.get_unallocated()
