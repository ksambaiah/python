#!/usr/bin/env python3

'''
  Computation pi = 4/1 - 4/3 + 4/5 - 4/7 + 4/9 ...
'''

def piCompute(num) -> float:

    numerator: float = 4.0
    denominator: float = 1.0
    operator: float = 1.0
    pi: float = 0.0

    for _ in range(num):
        pi += operator * ( numerator / denominator)
        denominator += 2
        operator *= -1.0
    return pi

if __name__ == '__main__':
    print(piCompute(3))
    print(piCompute(5))
    print(piCompute(10))
    print(piCompute(15))
    print(piCompute(10000000))
    print(piCompute(1000000000))
    print(piCompute(100000000000))
    print(piCompute(1000000000000000))
