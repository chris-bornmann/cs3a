
def raise_it(num, pow, acc):
    if pow == 0:
        return acc

    acc = raise_it(num, pow - 1, num * acc)
    return acc


def main():
    num = int(input('Enter number to raise to a power: '))
    pow = int(input('Enter power to raise it to: '))

    val = raise_it(num, pow, 1)
    print(val)


if __name__ == '__main__':
    main()
