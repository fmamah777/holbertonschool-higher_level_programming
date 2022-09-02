#!/usr/bin/python3
def element_at(my_list, idx):
    listlen = len(my_list)
    if idx < 0 or idx > listlen:
        return None
    for i in range(listlen):
        if i == idx:
            return my_list[i]
