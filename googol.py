# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 14:50:21 2024

@author: jcp
"""

# 구골(googol)은 10^100을 일컫는 말로, 1 뒤에 0이 백 개나 붙는 어마어마한 수입니다.
# 100^100은 1 뒤에 0이 2백 개가 붙으니 상상을 초월할만큼 크다 하겠습니다.
# 하지만 이 수들이 얼마나 크건간에, 각 자릿수를 모두 합하면 둘 다 겨우 1밖에 되지 않습니다.

# a, b < 100 인 자연수 a^b 에 대해서, 자릿수의 합이 최대인 경우 그 값은 얼마입니까?

max_sum = 0
for a in range(1, 100):
    for b in range(2, 100):
        sum = 0
        n = a**b
        while(n != 0):
            sum += (n % 10)
            n = n // 10
        if max_sum < sum:
            max_sum = sum

print(max_sum)

# %%
# a,b < 100 중 googol 중 가장 큰 값은?
googol = []
max = 0
max_sum = 0
for a in range(1, 100):
    for b in range(2, 100):
        sum = 0
        n = res = a**b
        while(n != 0):
            sum += (n % 10)
            n = n // 10
        if sum==1:
            googol.append((a,b))
            max = res
            
print(googol)
print(max)