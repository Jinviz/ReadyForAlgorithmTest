n, b = map(int, input().split())
max_root = 0
n_case = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

while True:
    if n / (b ** max_root) >= 1:
        max_root += 1
    else:
        break

calc_dump = n
quotient_dump, root_dump = [[0 for _ in range(max_root)] for _ in range(2)]

for i in range(max_root - 1, -1, -1):
    if calc_dump / (b ** i) >= 1:
        quotient, remainder = divmod(calc_dump, b ** i)
        calc_dump = remainder
        quotient_dump[i] = quotient
        root_dump[i] = 1

result = ''.join([n_case[num] for num in quotient_dump if num != 0])
print(result)




# 잘못된 풀이
# n, b = map(int, input().split())
# max_root, quotient, remainder = 0, 0, 0
# root_list, letter = [], []
# n_case = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# while True:
#     if n / (b**max_root) >= 1:
#         max_root += 1
#     else: 
#         break

# calc_dump = n
# quotient_dump, root_dump = [[0 for _ in range(max_root+1)] for _ in range(2)]

# for i in range(max_root, -1, -1):
#     if calc_dump / (b**i) >= 1:
#         quotient, remainder = divmod(n, b**i)
#         calc_dump = remainder
#         quotient_dump[i] = quotient
#         root_dump[i] = 1


# for k in range(max_root+1):
#     letter.append(n_case[quotient_dump[k]])

# result = ''.join(letter)
# print(result)