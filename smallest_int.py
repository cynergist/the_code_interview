#!/usr/bin/python
def find_smallest_int(arr):
    ''' Method finds the smallest integer in an array '''
    arr.sort()
    return (arr[:1]).pop()
print(find_smallest_int([4, 9, 100, 0]))
print(find_smallest_int([78, 56, -2, 12, 8, -33]))
print(find_smallest_int([0, 1 - 2**6, 2**6]))

