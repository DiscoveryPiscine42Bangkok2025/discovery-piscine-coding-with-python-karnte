#!/usr/bin/env python3

num = float(input("Give me a number: "))
int_part = int(num)

if num == int_part:
    print(int_part)
else:
    if num > 0:
        print(int_part + 1)
    else:
        print(int_part)
