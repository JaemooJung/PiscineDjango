def print_numbers():
    try:
        with open('./numbers.txt', 'r') as file:
            numbers = file.read()
        numbers_list = numbers.split(',')
        for number in numbers_list:
            print(number)

    except FileNotFoundError:
        print('File not found')

if __name__ == '__main__':
    print_numbers()