N = int(input())
cow = {n+1: -1 for n in range(10)}
count = 0

for _ in range(N):
    cow_num, cow_pos = map(int, input().split())
    if cow[cow_num] != -1 and cow[cow_num] != cow_pos:
        count += 1    
    cow[cow_num] = cow_pos

print(count)