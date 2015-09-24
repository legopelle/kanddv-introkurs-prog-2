'''
Information Technology (1DT051) 2015

Programming assignment 2.

A collection of mandatory exercises on the following topics:

 * Lists and strings.

 * Indexing lists and strings.

 * Iteration over lists and strings.

 * Predicate functions, functions taking an argument and returning
   True of False.

 * Solving problems using iteration (for).

'''

__author__  = "Karl Marklund"
__email__   = "karl.marklund@it.uu.se"
__date__    = "2014-09-25"
__version__ = "0.2"

# In the module utils.py many useful functions on lists and strings
# are defined. Have a look at the source to see what's available. You
# don't need to understand all details.

# Import all functions from the utils module.

from utils import *

# ==========================================
# ==========  Functions on lists  ==========
# ==========================================

def length(xs):
    '''
    Arguments:

    xs :: list

    Returns :: int
        The number of elements in xs.
    '''

    n = 0

    # TODO: You must add code here. You may not use the built-in
    # function len().

    return n

def sum(ns):
    '''Arguments:

    ns :: list of numbers.

    Returns :: number (int or float)
        The sum of all numbers in ns.

    Examples:

    >>> sum([])
    0
    >>> l = [0, 1, 7, 66, 9, 10, 3]
    >>> sum(l)
    96

    '''

    s = 0

    # TODO: You must add code here.

    return s

def ith(xs, i):
    '''
    Arguments:

    xs :: list

    i :: int

    Returns:
        If i is a valid index, return the element at index i in xs.

    Examples:

    >>> l = ["a", "b", "c"]
    >>> ith(l, 0)
    'a'
    >>> ith(l, 1)
    'b'
    >>> ith(l, 2)
    'c'
    '''

    # TODO: You must add code here. Use square bracket notation to
    # get the value at index i in the list xs.

    return -999 # You must change this!

def set_ith(xs, i, value):
    '''Arguments:

    xs :: list

    i :: int

    value :: Any type of value.

    Returns:
        If i is a valid index, return xs but with the value of
        the element at index i in xs replaced with value.

    Side effects:
        The original list xs is updated in place.

    Examples:

    >>> l = ["a", "b", "c"]
    >>> set_ith(l, 1, "B")
    ['a', 'B', 'c']
    >>> set_ith(range(10), 3, "foo")
    [0, 1, 2, 'foo', 4, 5, 6, 7, 8, 9]
    >>>

    '''

    # TODO: You must add code here. Use square bracket notation and
    # index to update the list xs.


    return xs

def take(n, xs):
    '''
    Arguments:

    n :: int

    xs :: list

    Returns :: list
        A new list with the n first consecutive elements from xs.
        If there is not enough elements in xs, the new list
        will have less than n elements.

    Examples:

    >>> l = [0,1,2,3,4]
    >>> take(0, l)
    []
    >>> take(1, l)
    [0]
    >>> take(2, l)
    [0, 1]
    >>> take(32, l)
    [0, 1, 2, 3, 4]
    '''

    return xs # You must change this! Use slice notation.


# ===========================================
# ========== Iteration over lists  ==========
# ===========================================

def print_all(xs):
    '''
    Arguments:

    xs :: list

    Side effects:
        Print each element x in xs  on a separate line.

    Example:

    >>> l = [1, 2, 3]
    >>> print_all(l)
    1
    2
    3
    '''

    print "To be implemented" # You must change this!


def print_double(ns):
    '''
    Arguments:

    ns :: list of int or float

    Side effects:
        For each element n in ns, prints 2*n on a separate line.

    Example

    >>> l = [1, 2, 3]
    >>> print_double(l)
    2
    4
    6
    '''

    print "To be implemented" # You must change this!


def max(ns):
    """
    Arguments:

    ns :: list of numbers

    Returns the largest number in ns. Returns None if ns is empty.

    Example:

    >>> ns = [9, 2, 1, 17, 2, 11]
    >>> max(ns)
    17
    """

    max = None

    # TODO: You must add code here.

    # NOTE: Your solution should use iteration (for).


    return max

# ==========================================
# ========== Predicate functions  ==========
# ==========================================

# NOTE: A predicate functions takes a single argument and returns a boolean
# value (True or False).

def is_odd(n):
    '''
    Arguments:

    n :: int

    Return :: bool
        If n is odd, returns True and otherwise returns False.

    Example:
    >>> is_odd(0)
    False
    >>> is_odd(1)
    True
    is_odd(2)
    False
    '''

    return True # You must change this!

def is_even(n):
    '''
    Arguments:

    n :: int

    Return :: bool
        If n is even, returns False and otherwise returns True.

    Example:

    >>> is_even(0)
    True
    >>> is_even(1)
    False
    >>> is_even(2)
    True
    '''

    # TODO: You use should is_odd() as part of your solution.

    return True # You must change this!

def print_odd(ns):
    '''
    Arguments:

    ns :: list of of integers

    Side effects:
        Prints all odd numbers in ns on a separate line.

    Example:

    >>> l = [0, 1, 7, 66, 9, 10, 3]
    >>> print_odd(l)
    1
    7
    9
    3
    '''

    print "To be implemented" # TODO: You must change this.


def print_even(ns):
    '''
    Arguments:

    ns :: list of of integers

    Side effects:
        Prints all even numbers in ns on a separate line.

    Example:

    >>> l = [0, 1, 7, 66, 9, 10, 3]
    >>> print_evenl)
    0
    66
    10
    '''

    print "To be implemented" # TODO: You must change this.

