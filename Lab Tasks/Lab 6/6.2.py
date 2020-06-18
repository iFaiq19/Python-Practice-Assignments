# Write a program that take a user input and to create the multiplication table (from 1 to 10) of that number.

x = int(input('Enter #: '))
for i in range(1,11):
    print(x, '\tx\t', i, '\t=\t', i*x)