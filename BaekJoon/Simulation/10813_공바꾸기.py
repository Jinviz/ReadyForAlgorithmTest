import sys
input = sys.stdin.readline

N, M = map(int, input().split())
basket = [n+1 for n in range(N)]

for _ in range(M):
    i, j = map(int, input().split())
    temp = basket[i-1]
    basket[i-1] = basket[j-1]
    basket[j-1] = temp

print(' '.join(map(str, basket)))
