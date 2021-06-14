#!/usr/bin/env python3

def isPalindrome( x: int) -> bool:
       y = 0
       x1 = x
       while x:
           y = x % 10 + y * 10
           x = x // 10
       if x1 == y:
           return True
       else:
           return False

if __name__ == '__main__':
    print(1234)
    print(isPalindrome(1234))
    print(1221)
    print(isPalindrome(1221))
