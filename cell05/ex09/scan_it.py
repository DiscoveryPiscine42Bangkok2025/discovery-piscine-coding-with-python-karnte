#!/usr/bin/env python3
from sys import argv

if len(argv) != 3:
    print("none")
else:
    word = argv[1]
    string = argv[2]
    print(string.count(word))