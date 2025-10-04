import sys
input = sys.stdin.readline

N, M = map(int, input().split())
basket = [n+1 for n in range(N)]  # [1, 2, ..., N]

for _ in range(M):
    i, j = map(int, input().split())
    basket[i-1:j] = reversed(basket[i-1:j])

print(' '.join(map(str, basket)))
