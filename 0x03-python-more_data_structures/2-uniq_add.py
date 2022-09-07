#!/usr/bin/python3
def uniq_add(my_list=[]):
    answer = 0
    for y in set(my_list):
        answer += y
    return (answer)
