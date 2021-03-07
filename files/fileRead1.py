#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: samkilar
"""

# This is nice way to learn try finally.
try:
    f = open('./testfile.txt')
    for line in f:
        line = line.strip()
        # Process the line
        print(line)
finally:
    f.close()
