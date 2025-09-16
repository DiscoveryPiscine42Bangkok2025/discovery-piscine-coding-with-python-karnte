#!/usr/bin/env python3
num = float(input("Give me a number : "))
try:
    if num % 1 == 0:
        print("This number is an integer.")
    else:
        print("This number is a decimal.")
except ValueError:
    print("Invalid input.")