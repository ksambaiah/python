#!/usr/bin/env python3
import sys

# Fib number computation

def fibonaci(n):
   if n in fibno :
      return(fibno[n])
   if n == 0 or n == 1 :
      value = 1
   else:
      value  = fibonaci(n-1) + fibonaci(n-2)
   fibno[n] = value
   return(value)


if __name__  == '__main__':
   # Takes integer from the user input and prints fibonacii numbers
   fibn = int(input("Enter integer : "))
   fibno = {}
   if isinstance(fibn, int):
       value = fibonaci(fibn)
       print("Value of fib of {0} is {1} \n".format(fibn, value))
   else:
       print("You need to give integer number")
       sys.exit(1)
