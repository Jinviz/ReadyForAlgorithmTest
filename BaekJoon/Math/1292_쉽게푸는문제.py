start, end  = map(int,input().split())
L = []
count = 1
sum = 0

while len(L) < end:
  for _ in range(count):
    L.append(count)
  count += 1

for n in range(start-1, end):
  sum += L[n]
  
print(sum)