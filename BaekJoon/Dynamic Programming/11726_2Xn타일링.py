import sys

N = int(sys.stdin.readline())
MOD = 10007

D = [0] * (N + 2)
D[1] = 1
D[2] = 2

for i in range(3, N + 1):
    D[i] = D[i - 1] + D[i - 2] % MOD 

print(D[N] % MOD)
