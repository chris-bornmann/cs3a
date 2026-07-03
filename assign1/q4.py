"""
CS03A - Summer 2026
Assignment 1 - Question 4
Student Name: Chris Bornmann
SID: 20743473
"""

from decimal import Decimal, ROUND_HALF_UP

"""
We use Decimal instead of float to remove inaccuracies of float that would
cause the value to deviate.  We are interested in a currency, so Decimal is
the best choice.
"""

BASE_TUITION = Decimal(8000)                 # Starting tuition
YEARLY_PERCENT_INCREASE = Decimal(3 / 100)   # Increase as a fraction!
NUMBER_OF_YEARS = 5                          # Prognosticate out this far.

def run():
    # Starting value is the current base.
    tuition = BASE_TUITION

    # Iterate through each year and show the cost for that year.
    for year in range(1, NUMBER_OF_YEARS + 1):
        tuition = tuition + (tuition * YEARLY_PERCENT_INCREASE)
        tuition = tuition.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        print(f'Year {year}: {tuition}')

if __name__ == "__main__":
    # This allows students to run this specific file 
    # individually for testing (e.g., `python q1.py`)
    run()
