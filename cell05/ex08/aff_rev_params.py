#!/usr/bin/env python3
from sys import argv

params = argv[1:]

if len(params) < 2:
    print("none")
else:
    for p in reversed(params):
        print(p)