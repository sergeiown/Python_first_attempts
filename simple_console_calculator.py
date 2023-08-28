user_choice = ''
while user_choice != 'e':
    def add(x, y):
        return x + y

    def subtract(x, y):
        return x - y

    def multiply(x, y):
        return x * y

    def divide(x, y):
        if y == 0:
            print('\nZero division is impossible!')
            return None
        return x / y

    def exponentiate(x, y):
        return x ** y

    def input_number(prompt):
        try:
            return float(input(prompt))
        except ValueError:
            print('\nThe value you entered is not a number!')
            return None

    print("\033[H\033[J")
    print('''
Available arithmetic operations:

    +   - addition; 
    -   - subtraction;
    *   - multiplication;
    /   - division;
    ^   - exponentiation.
    ''')

    x = input_number('Enter the first number: ')
    y = input_number('Enter the second number: ')

    if x is None or y is None:
        user_choice = input('\nPress "Enter" to repeat:  ')
        continue

    operation = input('\nEnter the arithmetic operation from the available: ')
    result = None

    if operation == '+':
        result = add(x, y)
    elif operation == '-':
        result = subtract(x, y)
    elif operation == '*':
        result = multiply(x, y)
    elif operation == '/':
        result = divide(x, y)
    elif operation == '^':
        result = exponentiate(x, y)
    else:
        print('\nCurrent arithmetic operation is not supported!')
        user_choice = input('\nPress "Enter" to repeat:  ')

    if result is not None:
        print('\nThe result is: {:.2f}'.format(result), end='')
        user_choice = input(
            '\n\nType "e" to exit or press "Enter" to repeat:  ')
