M = int(input())
N = int(input())
decimal = []

for n in range(M, N+1):
  print(n)
  for m in range(2, n//2+1):
    if n % m == 0:
      break
    
    if m == n//2+1:
      decimal.append(n)

if len(decimal) == 0:
  print(-1)
else:
  print(sum(decimal))
  print(min(decimal))