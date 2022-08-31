#!/usr/bin/python3
for x in range(97, 123):
    if chr(x) in "eq":
        continue
    print("{}".format(chr(x)), end='')
