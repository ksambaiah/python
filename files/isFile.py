#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: samkilar
"""
import os
import sys


if not os.path.isdir("testfile.txt"):
    print("testfile.txt is not directory")

if not os.path.isfile("testfile.txt"):
    print("testfile.txt is not a file")
