import sys
N  = int(input())
case = [''.join(input().split()) for _ in range(N)]

count = {}

for per in case:
    for p in per:
        if p not in count:
            count[p] = 1
        else:
            count[p] += 1
    max_value = max(count.values())
    max_value_key = [key for key, value in count.items() if value == max_value]
    if len(max_value_key) > 1:
        print('?')
    else:
        print(max_value_key[-1])
    count = {}