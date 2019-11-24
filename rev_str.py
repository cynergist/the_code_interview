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
