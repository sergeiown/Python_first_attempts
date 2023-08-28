from datetime import datetime
import time


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


def main():
    print('Starting Fibonacci computation...')
    start_time = datetime.now()
    print('Result for the number "40" is ', fibonacci_recursion(40))
    print('---')
    time.sleep(1)
    print('Execution time using recursion:', datetime.now() - start_time, 's')

    print('---')
    start_time = datetime.now()
    time.sleep(1)
    print('Execution time using cycle:', datetime.now() - start_time, 's')


if __name__ == '__main__':
    main()
