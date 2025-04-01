N, K = map(int, input().split())

num = []

for n in range(1, N + 1):
  k = N % n
  if k == 0:
    num.append(n)

if len(num) < K:
  print(0)
else:
  print(num[K-1])