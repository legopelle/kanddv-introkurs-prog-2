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


print "Take"
print take(2, l)

print "Print All"
print_all(l)

print "Double print"
print_double([1, 2, 3, 4])

print "Max"
print max([-1, 2, -18])


print "is odd"
print is_odd(3)
print is_odd(4)

print "is even"
print is_even(3)
print is_even(4)

print "print odd"
print_odd([1, 2, 3, 4])

print "Print even"
print_even([1, 2, 3, 4])



# ==========================================================================
# ==========  Tests for the functions in the optional.py module.  ==========
# ==========================================================================

# TODO: Add suitable tests for att the functions in the optional.py module.
