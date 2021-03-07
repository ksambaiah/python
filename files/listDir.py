#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: samkilar
"""
import os
import sys

for f in os.listdir('/'):
      print(f)

#Listdir gives files also.
for f in os.listdir('/Users/samkilar'):
   print(f)

for curr_dir, subdirs, files in os.walk('/Users/samkilar/Desktop'):
   print(subdirs)
   print('D:', os.path.abspath(curr_dir))
   for subdir in subdirs:
        print('SD:', os.path.abspath(subdir))
   for file in files:
        print(os.path.join(os.path.abspath(curr_dir)), file)
