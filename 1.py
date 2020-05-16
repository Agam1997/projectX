# -*- coding: utf-8 -*-
"""
Created on Fri May 15 19:23:35 2020

@author: dubey
"""

#Calculator
# Input paramemeters a, b & type of operation

a = float(input("Please enter first number for a mathematical operation: "));
b = float(input("Please enter second number for a mathematical operation: "));
type_of_operation = str(input("Please specify type of operation: "))
c = str.lower(type_of_operation);

def add(a,b):
    sum1 = float;
    sum1 = (a + b);
    print("Sum of A & B is: ", sum1)

def sub(a,b):
    subs = float;
    subs = (a - b);
    print("Substraction of A & B is: ", subs)

def multi(a,b):
    multi = float;
    multi = (a * b);
    print("Multiplication of A & B is: ", multi)

def div(a,b):
    div = float;
    div = (a / b);
    print(round(div,3))

if c == "addition":
    add(a,b)
elif c == "substraction":
    sub(a,b)
elif c == "multiply":
    multi(a,b)
elif c == "division":
    div(a,b)
