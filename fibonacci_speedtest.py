from datetime import datetime
import time
import sys
import threading

# Recursive Fibonacci function


def fibonacci_recursion(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_recursion(n - 1) + fibonacci_recursion(n - 2)

# Iterative Fibonacci function


def fibonacci_cycle(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    a, b = 0, 1
    for i in range(n - 1):
        a, b = b, a + b
    return b

# Function to print a progress bar


def print_progress_bar(number):
    i = 0
    while i < number * 200:
        sys.stdout.write('.')
        sys.stdout.flush()
        i += 1
        if i % 58 == 0:
            sys.stdout.write('\r')
            sys.stdout.flush()

# Main program function


def main():
    # User input and validation loop
    while True:
        try:
            number = int(input('Please enter an integer between 2 and 42: '))
            if 2 <= number <= 42:
                break
            else:
                print('\nPlease enter a valid number.\n')
        except ValueError:
            print('\nPlease enter a valid number.\n')

    print(f'\nYou entered the number: {number}')

    print(
        '\nPerforming the calculation of the {0}th Fibonacci number...\n'.format(number))
    start_time = datetime.now()

    # Create a thread for printing progress
    progress_thread = threading.Thread(
        target=print_progress_bar, args=(number,))
    progress_thread.start()

    # Calculate Fibonacci using recursion
    result = fibonacci_recursion(number)
    time.sleep(1)
    progress_thread.join()

    sys.stdout.write('\n\nResult: ')
    sys.stdout.flush()
    print(result, '\n\n---\n')

    # Calculate execution time for recursion
    execution_time_recursion = (datetime.now() - start_time).total_seconds()
    minutes = int(execution_time_recursion // 60)
    seconds = (execution_time_recursion % 60) - 1
    formatted_time = f'{minutes} min {seconds:.0f} sec' if minutes > 0 else f'{seconds:.6f} sec'
    print('Execution time using recursion:', formatted_time, '\n\n---\n')

    # Calculate Fibonacci using iteration
    start_time = datetime.now()
    time.sleep(1)
    result = fibonacci_cycle(number)

    # Calculate execution time for iteration
    execution_time_cycle = (datetime.now() - start_time).total_seconds()
    minutes = int(execution_time_cycle // 60)
    seconds = (execution_time_cycle % 60) - 1
    formatted_time = f'{minutes} min {seconds:.0f} sec' if minutes > 0 else f'{seconds:.6f} sec'
    print('Execution time using cycle:', formatted_time, '\n\n---\n')

    input('Press Enter to continue...')


if __name__ == '__main__':
    # This block of code ensures that the 'main()' function is executed
    # only when this script is run directly (not when it's imported as a module).
    main()
