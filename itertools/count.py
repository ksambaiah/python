#!/usr/bin/env python3

'''
Example of count
'''

def count(start=0, step=1):
    # count(10) --> 10 11 12 13 14 ...
    # count(2.5, 0.5) -> 2.5 3.0 3.5 ...
    n = start
    while True:
        yield n
        n += step

if __name__ == '__main__':
    gen = count(20, 2)
    for i in gen:
        print(i) 
