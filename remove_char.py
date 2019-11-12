#!/usr/bin/python
def rm_char(char, string):
    ''' Method removes a given character from a string '''
    string = string.replace(char, "")
    return string
print(rm_char("o", "bookkeeper"))
print(rm_char("", "bookkeeper"))
print(rm_char("o", ""))