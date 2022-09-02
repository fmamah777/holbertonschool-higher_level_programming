#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    newlist = []
    for elem in my_list:
        if elem % 2 == 0:
            newlist.append(True)
        else:
            newlist.append(False)
    return newlist
