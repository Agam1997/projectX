# -*- coding: utf-8 -*-
"""
Created on Fri May 15 19:37:12 2020

@author: dubey
"""

p = input("Enter the length of the series: ")
g = int(float(p))
odd = []


def print_odd(g):
    g = int(g)
    for i in range(g * 2):
        if i % 2 == 1:
            odd.append(str(i))
        else:
            continue
    for item in odd:
        if item == odd[len(odd) - 1]:
            print(item, end="")
        else:
            print(item, end=', ')


print_odd(p)
