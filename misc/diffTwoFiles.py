#!/usr/bin/env python3

# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 17:42:47 2020

@author: samkilar
"""
import argparse
import sys

def difffile(s, d, diff=-200):
    try:
        src = open(s, 'r')
    except OSError:
        print("Could not open/read file:", s)
        sys.exit()
    try:
        dst = open(d, 'r')
    except OSError:
        print("Could not open/read file:", d)
        sys.exit()
    if diff != -200:
        try:
            diff = open(diff, 'w')
        except OSError:
            print("Could not write file:", diff)
            sys.exit()
    # Write program in stdout case later.
    srcfile  = src.read().splitlines() 
    dstfile  = dst.read().splitlines() 
    for s in set(srcfile)-set(dstfile):
        diff.write(s)
        diff.write("\n")
    src.close()
    dst.close()
    diff.close()



def get_args():
    parser = argparse.ArgumentParser(description='Demo of how argparse module works.')
    parser.add_argument('-s', dest='srcfile', help='Src file', required=True)
    parser.add_argument('-d', dest='destfile', help='Dest file', required=True)
    parser.add_argument('-f', dest='difffile', help='Diff file')
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    # Get arguments from command line.
    
    args = get_args()
    difffile(args.srcfile, args.destfile, args.difffile)
