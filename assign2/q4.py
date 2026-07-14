/*****************************************************/
/* CS03A - Summer 2026
/* Assignment 2 - Question 4
/* Student Name: Chris Bornmann
/* SID: 20743473
/***************************************************/


TEMPLATE = 'template.html'


def run():
    name = input('Enter your name: ')
    about = input('Describe yourself: ')

    template = open(TEMPLATE, 'r').read()
    html = template.format(name=name, about=about)

    with open('index.html', 'w') as f:
        f.write(html)


if __name__ == "__main__":
    # This allows students to run this specific file 
    # individually for testing (e.g., `python q1.py`)
    run()
