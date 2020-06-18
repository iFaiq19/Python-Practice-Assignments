# Write a Python program that prints all the numbers from 1 to 20 except 9 and 13

for num in range(1,21):
    if num == 9 or num == 13:
        continue
    else:
        print(num, end=' ')