#!/usr/bin/env python3
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x // y

num1 = int(input("Give me the first number: "))
num2 = int(input("Give me the second number: "))
print("Thank you!")

#add
print(f"{num1} + {num2} =", add(num1, num2))
#subtract
print(f"{num1} - {num2} =", subtract(num1, num2))
#multiply
print(f"{num1} * {num2} =", multiply(num1, num2))
#divine
print(f"{num1} / {num2} =", divide(num1, num2))
