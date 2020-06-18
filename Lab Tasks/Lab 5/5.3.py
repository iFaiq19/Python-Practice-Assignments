# Write a python program to lowercase first "n" characters in a string.

x = input('Enter a string: ')
y = int(input('Enter no. of letters: '))
print(x[0:y].lower() + x[y:])