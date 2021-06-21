#!/usr/bin/env python3
import re
a = "Thisissam"
c = a.split("i")
print(a)
print(c)
d = re.split('a|e|i|o|u', a)
print(d)
