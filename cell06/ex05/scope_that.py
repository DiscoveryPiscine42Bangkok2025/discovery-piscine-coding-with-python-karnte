#!/usr/bin/env python3
def add_one(n):
    return n + 1

num = 5
print("Before:", num)
add_one(num) 
print("After:", num) # didn’t assign this return value to anything

num = add_one(num) # assign it
print("Extra case:", num)