#!/usr/bin/env python3

'''
Given an array of numbers consisting of daily stock prices, calculate the maximum amount of profit that can be made from buying on one day and selling on another.

In an array of prices, each index represents a day, and the value on that index represents the price of the stocks on that day.
'''

def buy_and_sell_stock_once(prices):
    maxi = 0
    for i in range(len(prices)-1):
        curm = 0
        for j in range(i+1, len(prices)):
            curm =  prices[j]-prices[i]
            if curm < 0:
                break
            maxi = max(curm, maxi)
    return maxi
       
if __name__ == '__main__':
   a = [110,215,180,335,5]
   print(a)
   print(buy_and_sell_stock_once(a))
