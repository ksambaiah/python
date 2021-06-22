#!/usr/bin/env python3

'''
An axis-aligned rectangle is represented as a list [x1, y1, x2, y2], where (x1, y1) is the coordinate of its bottom-left corner, and (x2, y2) is the coordinate of its top-right corner. Its top and bottom edges are parallel to the X-axis, and its left and right edges are parallel to the Y-axis.

Two rectangles overlap if the area of their intersection is positive. To be clear, two rectangles that only touch at the corner or edges do not overlap.

Given two axis-aligned rectangles rec1 and rec2, return true if they overlap, otherwise return false.

'''
def isRectangleOverlap(rec1, rec2):
    if rec2[0] < rec1[2] and rec2[1] < rec1[3]:
        return True 
    return False


if __name__ == '__main__':
     rec1 = [5,15,8,18] 
     rec2 = [0,3,7,9]
     print(isRectangleOverlap(rec1, rec2))
