import re

def load_words(file_name):

    with open(file_name, 'r') as fp:
        content = fp.read()
    list_of_words = re.split('[ \r\n]', content)

    return list_of_words


def count_words(list_of_words):

    count_of_words = dict()
    for word in list_of_words:
        if len(word):
            if word in count_of_words:
                count_of_words[word] = count_of_words[word] + 1
            else:
                count_of_words[word] = 1

    return count_of_words


def show_words(count_of_words):
    words_in_order = dict(sorted(count_of_words.items(), key=lambda item: item[1]))
    for item in words_in_order:
        print(f'{item} appears {count_of_words[item]} times')


def main():
    file_name = input('Enter name of file: ')
    list_of_words = load_words(file_name)
    count_of_words = count_words(list_of_words)
    show_words(count_of_words)


if __name__ == '__main__':
    main()
