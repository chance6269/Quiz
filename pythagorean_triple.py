# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 14:27:58 2024

@author: jcp
"""


# 세 자연수 a, b, c 가 피타고라스 정리 a^2 + b^2 = c2 를 만족하면 피타고라스 수라고 부릅니다 (여기서 a < b < c ).
# 예를 들면 3^2 + 4^2 = 9 + 16 = 25 = 52이므로 3, 4, 5는 피타고라스 수입니다.

# a + b + c = 1000 인 피타고라스 수 a, b, c는 한 가지 뿐입니다. 이 때, a × b × c 는 얼마입니까?


for a in range(1, 333):
    for b in range(a+1, 1001-a):
        c = 1000 - a - b
        if a**2 + b**2 == c**2 and b < c:
            print('a, b, c의 값은', a, b, c, '입니다')
            print('a x b x c의 값은', a * b * c, '입니다')
            break