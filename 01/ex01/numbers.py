def print_numbers():
    with open('./numbers.txt', 'r') as file:
        numbers = file.read()

    numbers_list = numbers.split(',')

    for number in numbers_list:
        print(number) 

if __name__ == '__main__':
    print_numbers()