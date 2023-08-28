from datetime import datetime
import time
import sys
import threading


def fibonacci_recursion(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_recursion(n - 1) + fibonacci_recursion(n - 2)


def fibonacci_cycle(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    a, b = 0, 1
    for i in range(n - 1):
        a, b = b, a + b
    return b


def print_progress_bar(number):
    i = 0
    while i < number * 200:
        sys.stdout.write('.')
        sys.stdout.flush()
        i += 1
        if i % 58 == 0:
            sys.stdout.write('\r')
            sys.stdout.flush()


def main():
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

    progress_thread = threading.Thread(
        target=print_progress_bar, args=(number,))
    progress_thread.start()

    result = fibonacci_recursion(number)
    time.sleep(1)
    progress_thread.join()

    sys.stdout.write('\n\nResult: ')
    sys.stdout.flush()
    print(result, '\n\n---\n')

    execution_time_recursion = (datetime.now() - start_time).total_seconds()
    minutes = int(execution_time_recursion // 60)
    seconds = (execution_time_recursion % 60) - 1
    formatted_time = f'{minutes} min {seconds:.0f} sec' if minutes > 0 else f'{seconds:.6f} sec'
    print('Execution time using recursion:', formatted_time, '\n\n---\n')

    start_time = datetime.now()
    time.sleep(1)
    result = fibonacci_cycle(number)

    execution_time_cycle = (datetime.now() - start_time).total_seconds()
    minutes = int(execution_time_cycle // 60)
    seconds = (execution_time_cycle % 60) - 1
    formatted_time = f'{minutes} min {seconds:.0f} sec' if minutes > 0 else f'{seconds:.6f} sec'
    print('Execution time using cycle:', formatted_time, '\n\n---\n')

    input('Press Enter to continue...')


if __name__ == '__main__':
    main()
