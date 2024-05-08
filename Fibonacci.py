# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 09:21:54 2024

@author: jcp
"""

# 피보나치(Fibonacci) 수열의 각 항은 바로 앞의 항 두 개를 더한 것입니다. 1과 2로 시작하는 경우 이 수열은 아래와 같습니다.

# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# 4백만 이하의 짝수 값을 갖는 모든 피보나치 항을 더하면 얼마가 됩니까?

# 리스트 생성하는 버전
n = 4000000
fib=[]
fib.append(1)
fib.append(2)
i = 2
even_sum = fib[1]
odd_sum = fib[0]
while True:
    sum = fib[i-2] + fib[i-1]
    if sum > n:
        break
    fib.append(sum)
    i += 1
    if sum % 2 == 0:
        even_sum += sum
    else:
        odd_sum += sum

# %%
# 리스트 없이 결과만 보는 버전
n = 4000000

a = 1
b = 2
even_sum = b
odd_sum = a
while True:
    sum = a + b
    if sum > n:
        break
    a = b
    b = sum
    if sum % 2 == 0:
        even_sum += sum
    else:
        odd_sum += sum