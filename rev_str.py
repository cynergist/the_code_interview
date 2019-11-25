#!/usr/bin/python
def rev_str(string):
    ''' Method reverses a string using extended slice in step '''
    return(string[::-1])

print(rev_str("part"))
print(rev_str("reward"))
print(rev_str(""))

def rev_str1(string):
    ''' Method reverses a string using loop to save chars to new string '''
    char = len(string) - 1
    new_str = ""
    while(char >= 0):
        new_str += string[char]
        char = char - 1
    return new_str

print(rev_str1("part"))
print(rev_str1("reward"))
print(rev_str1(""))

def rev_str2(string):
    ''' Method reverses a string using python's built-in method '''
    string = "".join(reversed(string))
    return string

print(rev_str2("part"))
print(rev_str2("reward"))
print(rev_str2(""))

def rev_str3(string):
    ''' Method reverses a string using recursion '''
    if len(string) == 0:
        return string
    return rev_str3(string[1:]) + string[0]

print(rev_str3("part"))
print(rev_str3("reward"))
print(rev_str3(""))

