#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 00:56:14 2020

@author: samkilar
"""

import re

while (1):
    ln = input("Enter some data: ")
    if re.match("(.*)(L|l)", ln):
        print(ln)
    if re.match("(.*)sam", ln):
        break