#!/usr/bin/env python3

# Remove duplicates from list

def rmdups(list1):
    list2 = []
    for x in list1:
        if  x not in list2:
            list2.append(x)
    return(list2)        

def rmdupsSet(list1):
     list2 = set(list1)
     return(list(list2))
if __name__ == '__main__':
    list1 = [1,2, 3, "a", "b", "c", "c", 2, 3, 1]
    print("Original list is ", list1)
    newlist = rmdups(list1)
    print("After removing duplicates ", newlist)
    newlist1 = rmdupsSet(list1)
    print("Remove dupes using sets ", newlist1)
