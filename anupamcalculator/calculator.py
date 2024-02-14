# calculator.py
# This module contains the calculator functions

# Import the math module
import math

# Define the calculator functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def sqrt(x):
    if x < 0:
        return "Error! Square root of a negative number."
    else:
        return math.sqrt(x)

def power(x, y):
    return x ** y

def sine(x):
    return math.sin(math.radians(x))

def cosine(x):
    return math.cos(math.radians(x))

def tangent(x):
    return math.tan(math.radians(x))

def logarithm(x, base):
    if x <= 0 or base <= 0 or base == 1:
        return "Error! Invalid input for logarithm."
    else:
        return math.log(x, base)

# calculating LCM
def lcm(a,b):
    L=a if a>b else b
    while L<=a*b:
        if L%a==0 and L%b==0:
            return L
        L+=1
 
# calculating HCF
def hcf(a,b):
    H=a if a<b else b
    while H>=1:
        if a%H==0 and b%H==0:
            return H
        H-=1