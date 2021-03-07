#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
test_fileinput.py: Process all the files given in the command-line arguments
Usage: test_fileinput.py file1, file2, file3, ...
"""
import fileinput

def main():
    """Get lines from all the file given in the command-line arguments (sys.argv)"""
    lineNumber = 0
    for line in fileinput.input():
        line = line.rstrip()   # strip the trailing spaces/newline
        lineNumber += 1
        print('{}: {}'.format(lineNumber, line))

if __name__ == '__main__':
    main()
