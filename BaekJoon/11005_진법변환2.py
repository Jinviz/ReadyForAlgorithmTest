n, b = map(int, input().split())
max_root, quotient, remainder = 0, 0, 0
root_list, letter = [], []
n_case = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

while True:
    if n / (b**(max_root+1)) >= 1:
        max_root += 1
    else: 
        break

calc_dump = n
quotient_dump = [0] * (max_root+1)

for i in range(max_root, -1, -1):
    quotient, remainder = divmod(calc_dump, b**i)
    quotient_dump[i] = quotient
    calc_dump = remainder


for k in range(max_root+1):
    letter.append(n_case[quotient_dump[k]])

result = ''.join(reversed(letter))
print(result)