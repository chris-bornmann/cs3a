#*****************************************************/
# CS03A - Summer 2026
# Assignment 3 - Question 3
# Student Name: Chris Bornmann
# SID: 20743473
#***************************************************/


def reverseDisplay(num, acc):
    if num == 0:
        print(acc)
    else:
        acc = acc + str(num % 10)
        reverseDisplay(num // 10, acc)


def run():

    # Assume we really start with an int because the assignment says that,
    # but could just be a string.
    num = int(input('Enter a number: '))

    # It would be better to return the reversed number and print it here,
    # but that's not what the function name implies.
    reverseDisplay(num, '')


if __name__ == "__main__":
    # This allows students to run this specific file 
    # individually for testing (e.g., `python q1.py`)
    run()
