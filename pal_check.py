#!/usr/bin/python
def pal_check(string):
    ''' Implement an algorithm that checks if a string is a permutation of a palindrome. '''
    for i in string:
        for k in string[-1]:
            if k != i:
                print("{} is not a palindrome".format(string))
                return string
            else:
                print("{} is a palindrome".format(string))
                return string
print(pal_check("rapid"))
print(pal_check("racecar"))
print(pal_check(""))
print(pal_check("ici5ici"))
