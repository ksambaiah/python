#!/usr/bin/env python3

import sys
import shlex

args_file = sys.argv[1]
args_data = file(args_file).read()
arguments = shlex.split(args_data)
print(arguments)
