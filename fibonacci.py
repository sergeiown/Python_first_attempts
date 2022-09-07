from datetime import datetime
import time


def fibonacci_recursion(n):
    if n <= 1:
        return 1
    return fibonacci_recursion(n - 1) + fibonacci_recursion(n - 2)


def fibonacci_cycle(n):
    a, b = 1, 2
    for i in range(n - 1):
        a, b = b, a + b
    return a


def main():
    start_time = datetime.now()
    print('result for the number "40" is: ', fibonacci_recursion(40), end='\n')
    time.sleep(1)
    print('execution time using recursion: ', datetime.now() - start_time, end='\n')

    start_time = datetime.now()
    fibonacci_cycle(40)
    time.sleep(1)
    print('execution time using cycle: ', datetime.now() - start_time, end='')


if __name__ == '__main__':
    main()
