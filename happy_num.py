# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 13:48:49 2024

@author: jcp
"""

# 판매하는 전기자동차 번호판 일련번호 4자리를 행복 수(happy number)로 채우고자 합니다.

# 행복 수는 각 자릿수의 제곱의 합으로 변환하는 과정을 반복할 때 언젠가는 1에 도달하는 수입니다.
# 예로, 13 → 1x1 + 3x3 = 10 → 1x1 + 0x0 = 1이므로 13은 행복 수입니다.

# 행복 수가 아닌 것은 슬픈(sad) 수 또는 불행(unhappy) 수라고 불립니다.
# 예로, 4 → 4x4 = 16 → 1x1 + 6x6 = 37 → 3x3 + 7x7 = 58 → ... → 4 로 순환하여 결코 1에 도달할 수 없으니 4는 슬픈 수입니다.

# 문제
# '얼른 마스크'씨 회사 전기자동차의 일련번호가 될 수 있는 1 ~ 9999 범위의 행복 수는 모두 몇 개이고
# 그 총합은 얼마인지 구하는 프로그램을 작성해서 보내주세요 작성하세요.


# 행복 수 체크

n = 13

res = 0
while (n != 0):
    res += (n % 10) ** 2
    n //= 10
    
check = 0
while(res != 0):
    check += (res % 10) ** 2
    res //= 10
    
cnt = 0
if check == 1:
    cnt += 1
    
print()
# %%
def happy_check(n):
    try:
        res = 0
        while (n != 0):
            res += (n % 10) ** 2
            n //= 10
        if res == 1:
            return 1
        return happy_check(res)
    except:
        return 0
# %%
def show_sum_cnt(n):
    happy_sum = 0
    cnt = 0
    for i in range(1, n+1):
        check = happy_check(i)    
        if check == 1:
            cnt += 1
            happy_sum += i
                
    print(f'1 ~ {n} 범위의 행복 수는 {cnt}개이고 총합은 {happy_sum}입니다.')

# %%

show_sum_cnt(9999)

happy_check(4)
