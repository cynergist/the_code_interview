#!/usr/bin/python
def char_count(string):
    ''' Method returns the number of occurrences of each characther in a given string '''
    mapp = {}
    for char in string:
        if char in mapp:
            mapp[char] += 1
        else:
            mapp[char] = 1
    return mapp
print(char_count("bookkeeper"))
print(char_count(""))
print(char_count("555-1234"))
