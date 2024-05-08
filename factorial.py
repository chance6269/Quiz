# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 12:31:08 2024

@author: jcp
"""

# 100!

# 10!

# 5! = 5 x 4 x 3 x 2 x 1

def factorial(n):
    
    result = 1
    for i in range(n):
        result *= (i + 1)
        
    return result

# %%

def factorial_rec(n):
    
    if n==1:
        return 1
    
    return n * factorial_rec(n-1)

# %%

# result = factorial(100)
result = factorial_rec(100)
sum = 0
while(result != 0):
    sum += (result % 10)
    result = result // 10
    
print(sum)

# %%

a = 100
b = a - 1
res = a
for i in range(b):
    res *= b
    b -= 1
    
    
