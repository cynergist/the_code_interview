#!/usr/bin/python
def urlify(string):
    ''' Simple method to replace all spaces in a string with '%20'. Remove any white space '''
    string = string.strip().replace(' ', '%20')
    return string
print(urlify("Ms Jane Smith     "))
print(urlify(""))
print(urlify("   html file  "))
