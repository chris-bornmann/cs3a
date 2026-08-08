#*****************************************************/
# CS03A - Summer 2026
# Assignment 3 - Question 1
# Student Name: Chris Bornmann
# SID: 20743473
#***************************************************/


import math


class Circle:

    def __init__(self):
        # This makes no sense.  Why not pass in arguments to set values?
        self._x = 0
        self._y = 0
        self._radius = 1

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, new_x):
        self._x = new_x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, new_y):
        self._y = new_y

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, new_radius):
        self._radius = new_radius

    def _distance(self, x, y):
        return math.sqrt((self._x - x) ** 2 + (self._y - y) ** 2)

    def getArea(self):
        return math.pi * self._radius * self._radius

    def getPerimeter(self):
        return 2 * math.pi * self._radius

    def containPoint(self, x, y):
        distance = self._distance(x, y)
        if distance < self._radius:
            return True
        return False

    def containCircle(self, circle):
        # If my radius is smaller or equal I can't possibly contain the other.
        if self._radius <= circle.radius:
            return False

        distance = self._distance(circle.x, circle.y)
        radii_diff = abs(self._radius - circle.radius)

        if distance <= radii_diff:
            # The equal means we treat "internally tangent" as "inside".
            return True
        return False

    def overlaps(self, circle):
        distance = self._distance(circle.x, circle.y)
        radii_sum = self._radius + circle.radius
        radii_diff = abs(self._radius - circle.radius)

        if (distance <= radii_sum) and (distance >= radii_diff):
            # Also includes if they fully overlap (same circle).
            return True

        return False


def run():
    circles = {'c1': Circle(), 'c2': Circle(), 'c3': Circle(), 'c4': Circle()}

    # Contains c1.
    circles['c2'].radius = 2

    # Overlaps c2.
    circles['c3'].x = 4
    circles['c3'].radius = 3

    # Doesn't touch anything.
    circles['c4'].x = 1000
    circles['c4'].y = 1000

    for key, val in circles.items():
        print(f'Circle {key}: Area = {val.getArea()}, Perimeter = {val.getPerimeter()}')
        if val.containPoint(5, 5):
            print(f'Circle {key} contains point (5, 5)')

        for key2, val2 in circles.items():
            if key != key2:
                if val.containCircle(val2):
                    print(f'Circle {key} contains circle {key2}.')
                if val.overlaps(val2):
                    print(f'Circle {key} overlaps circle {key2}.')


if __name__ == "__main__":
    # This allows students to run this specific file 
    # individually for testing (e.g., `python q1.py`)
    run()
