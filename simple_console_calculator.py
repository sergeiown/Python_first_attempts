user_choice = ''
while user_choice != 'e':
    # Function to perform addition
    def add(x, y):
        return x + y

    # Function to perform subtraction
    def subtract(x, y):
        return x - y

    # Function to perform multiplication
    def multiply(x, y):
        return x * y

    # Function to perform division
    def divide(x, y):
        if y == 0:
            print('\nZero division is impossible!')
            return None
        return x / y

    # Function to perform exponentiation
    def exponentiate(x, y):
        return x ** y

    # Function to input a number, handling potential errors
    def input_number(prompt):
        try:
            return float(input(prompt))
        except ValueError:
            print('\nThe value you entered is not a number!')
            return None

    # Clear the terminal screen
    print("\033[H\033[J")
    print('''
Available arithmetic operations:

    +   - addition; 
    -   - subtraction;
    *   - multiplication;
    /   - division;
    ^   - exponentiation.
    ''')

    # Input the first and second numbers
    x = input_number('Enter the first number: ')
    y = input_number('Enter the second number: ')

    # Check if the input is valid
    if x is None or y is None:
        user_choice = input('\nPress "Enter" to repeat:  ')
        continue

    # Input the desired arithmetic operation
    operation = input('\nEnter the arithmetic operation from the available: ')
    result = None

    # Perform the selected operation
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

    # Display the result if available
    if result is not None:
        print('\nThe result is: {:.2f}'.format(result), end='')
        user_choice = input(
            '\n\nType "e" to exit or press "Enter" to repeat:  ')
