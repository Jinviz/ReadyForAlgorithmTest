## 부루트 포스 풀이
sugar = int(input())
div, remain = divmod(sugar, 5) 
result = 0
cnt = 0

while True:
    if remain <= sugar:
        if remain % 3 == 0:
            result = (div - cnt) + remain / 3
            break
        else:
            cnt += 1
            remain = remain + 5 
    else:
        result = -1
        break

print(int(result))

## 모든 케이스를 생각하여 풀이

# div = math.floor(sugar / 5)
# remain = sugar % 5

# if div > 0:
#     if remain == 0: 
#         result = div   
#     elif remain == 1: 
#         if sugar >= 6:
#             result = div - 1 + 2
#         else:
#             result = -1
#     elif remain == 2:
#         if sugar >= 12:
#             result = div - 2 + 4 
#         else:
#             result = -1
#     elif remain == 3: 
#         result = div + 1
#     else:
#         result = div - 1 + 3
# else:
#     if remain == 3:
#         result = 1
#     else:
#         result = -1
