# Write a python program to sort a LIST of numbers in ascending order.

my_list = []
x = int(input('Enter # of elements in your list: '))
for i in range(x):
    y = int(input('Enter #: '))
    my_list.append(y)
print('List:', my_list)
for j in range(len(my_list)-1):
    for k in range(j+1, len(my_list)):
        if my_list[k] < my_list[j]:
            my_list[j] = my_list[j] + my_list[k]
            my_list[k] = my_list[j] - my_list[k]
            my_list[j] = my_list[j] - my_list[k]
print('Sorted List:', my_list)