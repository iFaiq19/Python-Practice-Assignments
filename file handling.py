"""Write a python program to create a file named employee.txt. Get input employee id, employee name and his / her salary
from user. Write this data to the file and then read that file."""
try:
    filee = open('employee.txt', 'x')
except FileExistsError:
    print('File with name employee.txt already exists.')
    a = int(input('Press (1) to overwrite the file or (2) to add data to the existing file. '))
    if a == 1: filee = open('employee.txt', 'w')
    elif a == 2: filee = open('employee.txt', 'a')
finally:
    lst1 = []
    x = int(input('Enter Number of Employees: '))
    for i in range(x):
        lis = []
        name = input('Enter Name of Employee #{}: '.format(i+1))
        lis.append(name)
        user_id = input('Enter Employee ID: ')
        lis.append(user_id)
        salary = input('Enter Salary: ')
        lis.append(salary)
        lst1.append(lis)
    for j in range(len(lst1)):
        filee.write('Employee Name:' + ' ' + lst1[j][0])
        filee.write('\nEmployee ID:' + ' ' + lst1[j][1])
        filee.write('\nSalary:' + ' ' + lst1[j][2])
        filee.write('\n')
    filee.close()
    filee = open('employee.txt', 'r')
    for k in filee:
        print(k)