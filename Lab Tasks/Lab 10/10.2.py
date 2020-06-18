"""Write a python program to count the number of occurence of each letter in word 'MISSISSIPPI' (or take input from user).
Store count of letters in a DICTIONARY"""

word = input('Enter a word: ')
dict_count = {}
for i in word:
    if i not in dict_count:
        dict_count[i] = 0
    dict_count[i] += 1
print(dict_count)