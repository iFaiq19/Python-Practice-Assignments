# Write a program that generates fibonacci series i.e. 1, 2, 3, 5, 8, 13, 21...

nterms = int(input('Enter # of Terms: '))
num1 = 1 ; num2 = 2
for i in range(nterms):
    print(num1, end=' ')
    n_num = num1 + num2
    num1 = num2
    num2 = n_num