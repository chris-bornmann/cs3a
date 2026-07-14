/*****************************************************/
/* CS03A - Summer 2026
/* Assignment 2 - Question 2
/* Student Name: Chris Bornmann
/* SID: 20743473
/***************************************************/

import math
import sys


def check_and_display_prime(num):

    # Assume true due to input check.
    assert num >= 2

    # Gross...  But, reduces # of checks.
    is_prime = all(num % i != 0 for i in range(2, int(math.sqrt(num)) + 1))
    if is_prime:
        print(f'{num} is prime.')
    else:
        print(f'{num} is composite.')


def run():

    upper_bound = int(input('How high should I go? '))
    if upper_bound < 2:
        print('Gotta be 2 or higher.')
        sys.exit(1)

    # It would be faster to check them all at the same time, and then
    # print the results, but this implementation follows the spec.
    nums_to_check = range(2, upper_bound + 1)
    for num in nums_to_check:
        check_and_display_prime(num)


if __name__ == "__main__":
    # This allows students to run this specific file 
    # individually for testing (e.g., `python q1.py`)
    run()
