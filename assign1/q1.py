"""
CS03A - Summer 2026
Assignment 1 - Question 1
Student Name: Chris Bornmann
SID: 20743473
"""

def run():
    """
    Students should implement their code for Question 1 inside this function.
    """

    principal = float(input('Please enter the principal: '))
    rate = float(input('Please enter the annual interest rate: '))
    cadence = int(input('Please enter the # of times per year interest is paid: '))
    duration = float(input('Please enter the # of years to calculate: '))

    amount = principal * (1 + (rate / 100) / cadence) ** (cadence * duration)

    print(f'Result: {amount:.2f}')

if __name__ == "__main__":
    # This allows students to run this specific file 
    # individually for testing (e.g., `python q1.py`)
    run()
