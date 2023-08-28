a = float(input('Enter the coefficient a: '))
b = float(input('Enter the coefficient b: '))
c = float(input('Enter the coefficient c: '))

d = b ** 2 - 4 * a * c

print('\nDiscriminant =', round(d, 2))

if a == 0:
    x = -c / b
    print('\nThis is a linear equation. One root: x =', round(x, 2))
else:
    if d < 0:
        print('\nDiscriminant is less than 0, there are no roots')
    else:
        if d == 0:
            x = -b / (2 * a)
            print('\nDiscriminant equals 0. One root: x =', round(x, 2))
        else:
            x1 = (-b + d ** 0.5) / (2 * a)
            x2 = (-b - d ** 0.5) / (2 * a)
            print('\nTwo roots: x1 =', round(x1, 2), 'and x2 =', round(x2, 2))

input("\nPress any key to exit...")
