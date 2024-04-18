people = int(input())
time = list(map(int, input().split()))
sort_time = sorted(time)
sum = 0
wait_time = 0

for p in range(people):
    wait_time += sort_time[p]
    sum += wait_time
    
print(sum)

