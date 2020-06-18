# Write a python program to swap the elements of two LIST without using a temporary LIST/variable.

list1 = []
list2 = []
x = int(input('Enter # of elements in the lists: '))
for i in range(2):
    for j in range(x):
        y = int(input('Enter # for List{}: '.format(i+1)))
        if i == 0:
            list1.append(y)
        else:
            list2.append(y)
print('List 1 = ', list1)
print('List 2 = ', list2)
for k in range(len(list1)):
    list1[k] = list1[k] + list2[k]
    list2[k] = list1[k] - list2[k]
    list1[k] = list1[k] - list2[k]
print('After Swap')
print('List 1', list1)
print('List 2', list2)