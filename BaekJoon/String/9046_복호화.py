import sys
N  = int(input())
case = [input().split() for _ in range(N)]

plain = "abcdefghijklmnopqrstuvwxyz"
password = "wghuvijxpqrstacdebfklmnoyz"

count = [{} for _ in range(N)]

for c in case:
    for i in c:
        plain.index(i)


for n, c in enumerate(case):
    for text in c:
        for t in text:
            if not count[n][t]:
                count[n][t] = 1
            else:
                count[n][t] += 1


