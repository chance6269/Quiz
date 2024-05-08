# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 17:17:45 2024

@author: jcp
"""

# 세 변의 길이가 모두 자연수 {a, b, c}인 직각삼각형의 둘레를 p 로 둘 때,
 # p = 120 을 만족하는 직각삼각형은 아래와 같이 세 개가 있습니다.

# {20, 48, 52}, {24, 45, 51}, {30, 40, 50}
# 1000 이하의 둘레 p에 대해서, 직각삼각형이 가장 많이 만들어지는 p의 값은 얼마입니까?

max_p=0
cnt=0
for p in range(4, 1001):
    n=0
    
    for c in range(p-2, p):
        for b in range(c-2, c):
            a = c - b
            if (a ** 2 + b ** 2) == c**2:
                n += 1
    if cnt < n:
        cnt = n
        max_p = p