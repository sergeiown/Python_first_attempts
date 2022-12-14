user_choice = 'y'
while user_choice != 'e':
    # Clearing the screen using ANSI/VT100 terminal control code sequences
    # \033 - ASCII escape character
    # [H - move the cursor to the home position
    # [J - erases the screen from the current line down to the bottom of the screen
    print("\033[H\033[J")
    print('''
Available arithmetic operations:

    +   - addition; 
    -   - subtraction;
    *   - multiplication;
    /   - division;
    ^   - exponentiation.
    ''')
    try:  # we check whether they are a number For each of the two entered values
        x = float(input('Enter the first number: '))
    except ValueError:
        print('\nThe value you entered is not a number!\nProgram interrupted.')
        break
    try:
        y = float(input('\nEnter the second number: '))
    except ValueError:
        print('\nThe value you entered is not a number!\nProgram interrupted.')
        break
    operation = input('\nEnter the arithmetic operation from the available: ')
    result = None

    if operation == '+':
        result = x + y
    elif operation == '-':
        result = x - y
    elif operation == '*':
        result = x * y
    elif operation == '/':  # Checking on 'Zero Division' and make the notice.
        try:
            x / y == 0
        except ZeroDivisionError:
            print('\nZero division is impossible!\nProgram interrupted.')
            break
        result = x / y
    elif operation == '^':
        result = x ** y
    else:
        print('\nCurrent arithmetic operation is not supported!')
        user_choice = input('\nPress "Enter" to repeat:  ')

    if result is not None:
        print('\nThe result is: ', result, end='')
        user_choice = input('\nType "e" to exit or press "Enter" to repeat:  ')
        
