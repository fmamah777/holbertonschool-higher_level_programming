#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    listlen = len(my_list)
    if idx < 0 or idx >= listlen:
        return my_list
    for i in range(listlen):
        if i == idx:
            my_list[i] = element
            return my_list
