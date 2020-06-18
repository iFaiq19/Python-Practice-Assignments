"""Write a program that generates the following pattern (using loop):
1
12
123
1234
12345"""

x = int(input('Enter # of Rows: '))
for i in range(1, x+1):
    for j in range(1, i+1):
        print(j, end='')
    print('')