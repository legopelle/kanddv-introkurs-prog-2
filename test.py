'''
Information Technology (1DT051) 2015

Programming assignment 2.

Tests for the functions in the mandatory.py and the optional.py modules.
'''

# Import all functions from the mandatory.py module.
from mandatory import *

# Import functions from the optional.py module.
from optional import *


# ===========================================================================
# ==========  Tests for the functions in the mandatory.py module.  ==========
# ===========================================================================

print "List length"

print length([])

print length([1, 2, 3])

# Use the # symbol to comment out tests you don't want to run.

print "Sum function"

print sum([])

print sum(range(10))

# TODO: Add suitable tests for all the functions in mandatory.py
# module.


print "extract element from list"

l = ["a", "b", "c"]
print ith(l, 2)
print ith(l, 0)

print "Change element in list"

print set_ith(l, 1, "buu")




# ==========================================================================
# ==========  Tests for the functions in the optional.py module.  ==========
# ==========================================================================

# TODO: Add suitable tests for att the functions in the optional.py module.
