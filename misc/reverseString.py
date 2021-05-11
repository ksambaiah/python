#!/usr/bin/env python3

# Reverse the words separated by space

if __name__ == '__main__':
    # Take the input, split it and reverse
    stringInput = input("Enter some data ")
    list1 = stringInput.split(" ")
    revString = " ".join(list1[::-1])
    print(revString)
