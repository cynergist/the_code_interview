#!/usr/bin/python
def fizz_buzz(start, stop):
    ''' Method implements a loop to solve fizz buzz on a given range of numbers '''
    for num in range(start, stop):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)
    return
print(fizz_buzz(1, 101))
