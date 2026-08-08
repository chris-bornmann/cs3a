#*****************************************************/
# CS03A - Summer 2026
# Assignment 3 - Question 2
# Student Name: Chris Bornmann
# SID: 20743473
#***************************************************/


class Employee:
    def __init__(self):
        self._name = 'unknown'
        self._number = 'unknown'

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, new_number):
        self._number = new_number


class ProductionWorker(Employee):

    def __init__(self):
        self._shift = 0
        self._pay = 0

    @property
    def shift(self):
        return self._shift

    @shift.setter
    def shift(self, new_shift):
        if new_shift not in [1, 2]:
            raise ValueError('Invalid shift number')

        self._shift = new_shift

    @property
    def pay(self):
        return self._pay

    @pay.setter
    def pay(self, new_pay):
        self._pay = new_pay


def run():
    print("Let's create a Production Worker!")
    name = input('Enter name: ')
    number = input('Enter number: ')
    shift = int(input('Enter shift [1 or 2]: '))
    pay = float(input('Enter hourly pay: '))

    sw = ProductionWorker()
    sw.name = name
    sw.number = number
    sw.shift = shift
    sw.pay = pay

    print('You entered:')
    print(f'{sw.name} / {sw.number}')
    print(f'Shift: {sw.shift}')
    print(f'Pay: {sw.pay}')


if __name__ == "__main__":
    # This allows students to run this specific file 
    # individually for testing (e.g., `python q1.py`)
    run()
