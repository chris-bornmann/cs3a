import sys


NUM_TO_GET = 20


def main():
    numbers = []

    print(f'Please enter {NUM_TO_GET} numbers, separated by spaces.')
    user_input = input('> ')

    numbers = user_input.split(' ')
    if len(numbers) < NUM_TO_GET:
        print(f"You didn't enter {NUM_TO_GET} numbers.  Please try again.")
        sys.exit(-1)

    # Are they legit?
    for item in numbers:
        if not item.isdigit():
            print(f'{item} is not a number.  Please try again.')
            sys.exit(-1)

    # Convert from strings to ints.
    numbers = list(map(int, numbers))

    # Perform calculations.
    minimum = min(numbers)
    maximum = max(numbers)
    sum_of_num = sum(numbers)
    average = sum_of_num / len(numbers)

    # Display the results.
    print(f'Minimum: {minimum}')
    print(f'Maximum: {maximum}')
    print(f'Sum: {sum_of_num}')
    print(f'Average: {average}')


if __name__ == '__main__':
    main()
