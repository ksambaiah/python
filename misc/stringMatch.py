#!/usr/bin/env python3

a = "SambaiahKilaru"
b = "Samksam"
if len(a) < len(b):
   max = len(a)
else:
   max = len(b)
i = 0
for j in  range(max):
    if a[j] == b[j]:
       i += 1
    else:
       break
print(i)
