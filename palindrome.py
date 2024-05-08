# -*- coding: utf-8 -*-
"""
Created on Fri May  3 10:43:31 2024

@author: jcp
"""

max_num = 0

for i in range(100, 1000):
    for j in range(100, 1000):
        n = i * j
        reversed_n = 0
        while n > 0:
            reversed_n *= 10
            reversed_n += n % 10
            n //= 10
        n = i * j
        if n == reversed_n:
            if n > max_num:
                max_num = n

print(max_num)

# %%

max_num = 0

for i in range(100, 1000):
    for j in range(100, 1000):
        n = i * j
        if str(n) == str(n)[::-1]:  
            if n > max_num:
                max_num = n

print(max_num)