# Implementation of PeterAnswers

import time
from msvcrt import getch
default = 'Please answer my question.'
i, z = 1, ''
print('Press \"ENTER\" to submit petition & question.')
print('Hint: Write \"Please answer my question.\" in petition column.')
print('Enter Your Petition Here: ', end='', flush=True)
while 1:
    x = getch()
    if ord(x) == 8:
        print('\b \b', end='', flush=True)
        i -= 1
    elif ord(x) == 13:
        break
    elif x.decode() != ',':
        print(x.decode(), end='', flush=True)
        i += 1
    elif x.decode() == ',':
        while x.decode() == ',':
            y = getch()
            print(default[i-1], end='', flush=True)
            i += 1
            if y.decode() == ',':
                break
            else:
                z += y.decode()
print('')
b = input('Ask Your Question: ')
if z == '':
    print('I only answer to Faiq!')
else:
    print('\nThinking your answer, wait a bit', end='')
    for i in range(3):
        print('.', end='', flush=True)
        time.sleep(1)
    print('')
    print('\nThe Answer to Your Question Is:', z)