from itertools import permutations
N = input()
num = []
sum = 0
for n in N:
    num.append(int(n))
    sum += int(n)
num.sort(reverse=True)

if sum % 3 == 0 and num[-1] == 0:
    print("".join(map(str, num)))
else:
    print(-1)
