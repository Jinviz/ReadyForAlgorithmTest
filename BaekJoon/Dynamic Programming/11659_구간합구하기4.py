import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [0] + list(map(int, input().split()))
P = [0] * (N+1)

for k in range(1, N + 1):
    P[k] = P[k - 1] + arr[k]

for m in range(M):
    i, j = map(int, input().split())
    result = P[j] - P[i-1]
    print(result)
