if __name__ == '__main__':
    print('hello world')
    number = int(input('Please insert your favorite number: '))

    while number <= 10:
        print('Too low')
        number = int(input('Please insert higher number: '))
    print('Good job!')