def get_num_of_characters(input_str):
    length = len(input_str)
    return length

def string_without_spaces(input_str):
    string = input_str.replace(" ", "")
    return string


if __name__ == '__main__':
    # Type your code here
    input_str = input('Enter a sentence or phrase:\n')
    print()
    print('You entered:', input_str, end='')
    print()
    print()
    print('Number of characters:', get_num_of_characters(input_str), end='')
    print()
    print('String with no whitespace:', string_without_spaces(input_str))