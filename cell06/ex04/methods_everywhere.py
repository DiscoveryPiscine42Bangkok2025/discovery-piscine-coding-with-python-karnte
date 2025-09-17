#!/usr/bin/env python3
from sys import argv

def shrink(s):
    return s[:8]

def enlarge(s):
    return s + "Z" * (8 - len(s))

if len(argv) < 2:
    print("none")
else:
    for arg in argv[1:]:
        if len(arg) > 8:
            print(shrink(arg))
        elif len(arg) < 8:
            print(enlarge(arg))
        else:
            print(arg)
