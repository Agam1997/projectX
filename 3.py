# -*- coding: utf-8 -*-
"""
Created on Fri May 15 19:50:55 2020

@author: dubey
"""
p = input("Enter the length of the series: ")
g = int(float(p))
odd = []


def print_odd(g):
    g = int(g)
    if g % 2 == 0:
        print_odd(str(g - 1))
    else:
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
