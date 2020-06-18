"""Write a python program which calculate whether the input number is prime or not but following conditions should be met:
>> First checks whether the number’s result is already stored in database or not.
>> If the number is already calculated earlier then it should fetch the result from database otherwise calculate the new
result and store it in database for future need."""
import mysql.connector
prime = mysql.connector.connect(host='localhost', user='ifaiq19', passwd='#*ifaiq19#*')
primecr = prime.cursor()
try:
    primecr.execute('CREATE DATABASE PrimeNum')
except mysql.connector.errors.DatabaseError:
    pass
finally:
    prime = mysql.connector.connect(host='localhost', user='ifaiq19',
                                    passwd='#*ifaiq19#*', database='PrimeNum')
    primecr = prime.cursor()
    try:
        primecr.execute('CREATE TABLE PrimeNum(Numbers VARCHAR(255), PrimeCheck VARCHAR(255))')
    except mysql.connector.errors.ProgrammingError:
        pass
    finally:
        num = int(input('Enter Number: '))
        n = 'SELECT PrimeCheck FROM PrimeNum WHERE Numbers= %s'
        value = num
        primecr.execute(n, (value,))
        check = primecr.fetchone()
        if check is not None:
            print('The number {} is already in our record and is'.format(num), check[0])
        else:
            x = 0
            y = 'Non-Prime Number'
            for i in range(2, num):
                if num % i != 0 or num == 2:
                    continue
                else:
                    x += 1
            if x == 0:
                y = 'Prime Number'
            else:
                y = 'Non-Prime Number'
            add = 'INSERT INTO PrimeNum (Numbers, PrimeCheck) VALUES (%s, %s)'
            val = (num, y)
            primecr.execute(add, val)
            prime.commit()
            print('Number {} which is a {} has been added to the record.'.format(num, y))
            print(primecr.rowcount, 'record inserted.')
