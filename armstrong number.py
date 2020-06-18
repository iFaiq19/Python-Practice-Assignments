"""Write a function called check_armstrong() that accepts one parameter as number. The function should return value
whether the entered number is an Armstrong number or not."""

# First Method


def check_armstrong(n):
    x, y = len(str(n)), 0
    for i in range(x):
        y += int(str(n)[i])**x
    return y


num = int(input('Enter Number: '))
if check_armstrong(num) == num:
    print(num, 'is an Armstrong Number')
else:
    print(num, 'is not an Armstrong Number')

# Second Method (Division)


def check_armstrong(num):
    digits, length = 0, len(str(num))
    while num > 0:
        var = num % 10
        digits += var**length
        num //= 10
    return digits


y= int(input('Enter Your Number: '))
if check_armstrong(y) == y:
    print('{} is an Armstrong Number'.format(y))
else:
    print('{} is not an Armstrong Number'.format(y))


