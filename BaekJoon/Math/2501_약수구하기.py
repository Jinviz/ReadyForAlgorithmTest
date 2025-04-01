N, K = map(int, input().split())

num = []

for n in range(1, N):
  k = N % n
  if k == 0:
    num.append(n)

if len(num)==0 or len(num) < K:
  print(0)
else:
  print(num[K-1])