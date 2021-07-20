#!/usr/bin/env python3

'''
Test break loop
'''


for i in range(10):
    print("i loop ", i)
    for j in range(5):
        print("j loop ", j)
        if j == 2:
           break
    if i == 3:
        break
        
