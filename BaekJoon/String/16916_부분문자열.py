import sys

P = sys.stdin.readline().rstrip()
S = sys.stdin.readline().rstrip()
result = 0
for n, p in enumerate(P):
    if p == S[0]:
        if S == P[n:n+len(S)]:
            result = 1
            break
    
print(result)