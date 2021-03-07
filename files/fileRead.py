#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: samkilar
"""

f = open("testfile.txt", "r")
line = f.readline()
while line:
    # Take out new line
    print(line.rstrip())
    line = f.readline()
f.close()
