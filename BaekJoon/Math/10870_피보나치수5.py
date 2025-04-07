N = int(input())
pre1, pre2 = 0, 1
temp = 0

for n in range(2, N+1):
  temp = pre1 + pre2
  pre1 = pre2
  pre2 = temp

print(pre2)

