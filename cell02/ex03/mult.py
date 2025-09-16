#!/usr/bin/env python3
num1 = int(input("Enter the first number:\n"))
num2 = int(input("Enter the second number:\n"))
result = num1 * num2

print("%d X %d = %d" % (num1, num2, result))
if result < 0:
    print("This number is negetive.")
elif result > 0:
    print("This number is positive.")
else:
    print("This number is positive and negative.")
