import sys


# Seat costs by class.
SEAT_COSTS = {
    'A': 20,
    'B': 15,
    'C': 10,
}


def calc_revenue():
    revenue = 0

    # What if they don't enter an integer?  Give up and make them start
    # over again.
    try:
        for item in SEAT_COSTS:
            num_seats = int(input(f'How many class {item} seats? '))
            revenue = revenue + num_seats * SEAT_COSTS[item]
    except Exception as ex:
        print(f'Ouch!  {ex}')
        print('Please try again.')

        # Non-zero error code to indicate error.
        sys.exit(1)

    return revenue


def main():
    revenue = calc_revenue()
    print(f'Total revenue: ${revenue}')


if __name__ == '__main__':
    main()
