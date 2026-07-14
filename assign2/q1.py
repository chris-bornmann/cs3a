/*****************************************************/
/* CS03A - Summer 2026
/* Assignment 2 - Question 1
/* Student Name: Chris Bornmann
/* SID: 20743473
/***************************************************/


GRAVITY = 9.8


def falling_distance(seconds):

    # The number of meters an object falls on Earth in seconds.

    distance = 0.5 * (GRAVITY * (seconds ** 2))
    return distance


def run():

    for seconds in range(1, 11):
        distance = falling_distance(seconds)
        print(f'Fell {distance:.1f} meters in {seconds} seconds.')


if __name__ == "__main__":
    # This allows students to run this specific file 
    # individually for testing (e.g., `python q1.py`)
    run()
