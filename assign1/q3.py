"""
CS03A - Summer 2026
Assignment 1 - Question 3
Student Name: Chris Bornmann
SID: 20743473
"""

def run():
    seconds = int(input('Please enter some # of seconds: '))

    minutes = hours = days = 0

    if seconds > 59:
        minutes = seconds // 60
        seconds = seconds % 60

    if minutes > 59:
        hours = minutes // 60
        minutes = minutes % 60

    if hours > 23:
        days = hours // 24
        hours = hours % 24

    print(f'{days} days, {hours} hours, {minutes} minutes, {seconds} seconds')
        

if __name__ == "__main__":
    # This allows students to run this specific file 
    # individually for testing (e.g., `python q1.py`)
    run()
