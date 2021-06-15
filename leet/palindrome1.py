#!/usr/bin/env python3

def isPalindrome(x: int) -> bool:
        x = abs(x)
        y = 0
        temp = x
        while temp:
            y = temp % 10 + y * 10
            temp = temp // 10
        if x == y:
            return True
        return False

if __name__ == '__main__':
    print(121)
    print(isPalindrome(-121))
    print(1221)
    print(isPalindrome(1221))
