"""
CS03A - Summer 2026
Assignment 1 - Question 2
Student Name: Chris Bornmann
SID: 20743473
"""

def run():
    month = int(input('Please enter a numeric month: '))
    day = int(input('Please enter a number day in that month: '))
    year = int(input('Please enter a two digit year: '))

    val = month * day
    if val == year:
        print('magic')
    else:
        print('not magic')

if __name__ == "__main__":
    # This allows students to run this specific file 
    # individually for testing (e.g., `python q1.py`)
    run()
