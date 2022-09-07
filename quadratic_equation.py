a = float(input('a: '))
b = float(input('b: '))
c = float(input('c: '))
d = b ** 2 - 4 * a * c
print('discriminant =', d)
if a == 0:
    x1 = x2 = (-c / b)
    print('x1 = x2 =', x1)
else:
    if d < 0:
        print("discriminant < 0 and we can't fined x")
    else:
        if d == 0:
            x1 = b * b / (2 * a)
            x2 = -b * b / (2 * a)
            print('x1 =', x1, 'and x2 =', x2)
        else:
            x1 = (-b + (d ** 0.5))/(2 * a)
            x2 = (-b - (d ** 0.5))/(2 * a)
            print('x1 =', x1, 'and x2 =', x2)
