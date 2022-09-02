#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    listlen = len(my_list)
    if idx < 0 or idx >= listlen:
        new_list = my_list.copy()
        return new_list
    new_list = my_list.copy()
    for i in range(len(new_list)):
        if i == idx:
            new_list[i] = element
            return new_list
