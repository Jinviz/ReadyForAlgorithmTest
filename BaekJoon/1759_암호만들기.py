# 최소 한개 모음, 최소 두개 자음, 오름차순
from itertools import combinations
L, C = map(int, input().split())
alpha = input().split()
vowel = "aeiou"
result = []
alpha_combs = combinations(sorted(alpha), L) # 조합과 오름차순 적용

for alpha_comb in alpha_combs:
    vowel_cnt = 0
    vowel_not_cnt = 0
    for alpha_comb_element in alpha_comb:
        if alpha_comb_element in vowel:
            vowel_cnt += 1
        else:
            vowel_not_cnt += 1
    if vowel_cnt >= 1 and vowel_not_cnt >= 2:
        result.append(''.join(alpha_comb))

# 출력
for answer in result:
    print(''.join(sorted(answer)))



# L, C = map(int, input().split())
# alpha = input().split()
# vowel = ['a', 'e', 'i', 'o', 'u']
# total = []
# case = []
# cnt = 0

# Combination(alpha, cnt, case)

# # 조합(재귀) 직접 구현 시도
# def Combination(dump_alpha, count, dump_case):
#     cnt = count + 1
#     if cnt <= L:
#         for a in dump_alpha: 
#             dump_case.append(a)
#             dump_alpha.remove(a)
#             Combination(dump_alpha, cnt, dump_case)
#     else:
#         total.append(dump_case)
#         cnt = 0

