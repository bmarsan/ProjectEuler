"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
import sys


def is_pythagorean_tuple(a_value, b_value, c_value):
    """
    Checks if the numbers in the provided list are a pythagorean tuple.
    :param a_value:
    :param b_value:
    :param c_value:
    :return boolean:
    """
    if (a_value**2) + (b_value**2) == (c_value**2):
        return True

    return False


sum_val = 1000
a_val = 1
b_val = 2
c_val = sum_val - a_val - b_val

for a_val in range(1, 499):
    while b_val < c_val:
        c_val = sum_val - a_val - b_val
        if is_pythagorean_tuple(a_val, b_val, c_val):
            print('a: {0}, b: {1}, c: {2}'.format(a_val, b_val, c_val))
            print(a_val*b_val*c_val)
            sys.exit()
        b_val += 1
    b_val = a_val + 2
