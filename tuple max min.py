# Write a python program to find maximum and minimum value (in numbers) within TUPLE

x, tuplee = int(input('Enter Number of Elements: ')), []
for i in range(x):
    z = int(input('Enter Number: ')); tuplee.append(z)
tuplee = tuple(tuplee)
maximum = tuplee[0]; minimum = tuplee[0]
for i in tuplee:
    if i >= maximum: maximum = i
    elif i <= minimum: minimum = i
print('Max=', maximum,'Min=', minimum)