# The following questions are extracted from CS61A Summer 2023 HW01
# These questions serve as a good practice for control statements in Python

# Question 1
# Fill in the blanks in the following function for adding a to the absolute value of b, 
# without calling abs. You may not modify any of the provided code other than the two blanks.
# Please also write tests for these functions
def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    >>> a_plus_abs_b(-1, 4)
    3
    >>> a_plus_abs_b(-1, -4)
    3
    """
    if b < 0:
        f = _____
    else:
        f = _____
    return f(a, b)

# Question 2
# Write a function that takes three positive numbers as arguments and returns the sum of the squares of the two smallest numbers. 
# Use only a single line for the body of the function.
def two_of_three(i, j, k):
    """Return m*m + n*n, where m and n are the two smallest members of the
    positive numbers i, j, and k.

    >>> two_of_three(1, 2, 3)
    5
    >>> two_of_three(5, 3, 1)
    10
    >>> two_of_three(10, 2, 8)
    68
    >>> two_of_three(5, 5, 5)
    50
    """
    return _____