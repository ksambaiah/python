#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 17:42:47 2020

@author: samkilar
"""


import argparse


def get_args():
    parser = argparse.ArgumentParser(description='Demo of how argparse module works.')
    parser.add_argument('-a', dest='appid', help='appid of application REQUIRED', required=True)
    parser.add_argument('-f', dest='file', help='filename to write data  REQUIRED', required=True)
    parser.add_argument('-g', dest='guard', help='guard to limit')
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    # Get arguments from command line.
    
    args = get_args()
    print(args)
    print("Appid ", args.appid, " file ", args.file)
