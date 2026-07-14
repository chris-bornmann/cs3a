/*****************************************************/
/* CS03A - Summer 2026
/* Assignment 2 - Question 3
/* Student Name: Chris Bornmann
/* SID: 20743473
/***************************************************/


def capitalize(uncapped):

    fixed_string = ''

    sentences = uncapped.split('.')
    for sentence in sentences:
        if sentence == '':
            # Preserve lone "."s for things like "...".
            fixed_string = fixed_string.strip() + '.'
        else:
            temp = sentence.strip()
            temp = temp[0].upper() + temp[1:]
            fixed_string = f'{fixed_string}{temp}.  '

    # Get rid of pesky trailing '  '.
    return fixed_string.strip()


def run():
    uncapped = input('Please enter a string: ')
    capped = capitalize(uncapped)
    print(capped)


if __name__ == "__main__":
    # This allows students to run this specific file 
    # individually for testing (e.g., `python q1.py`)
    run()
