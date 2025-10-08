N = int(input())
D = [0] * (N+1)
pre = [0] * (N+1)
n = 2

while n <= N:
    D[n] = D[n-1] + 1
    pre[n] = n-1
    if n%2==0:
        D[n] = min(D[n//2] + 1, D[n])
        if D[n] == D[n//2] +1:
            pre[n] = n//2

    if n%3==0: 
        D[n] = min(D[n//3] + 1, D[n])
        if D[n] == D[n//3] +1:
            pre[n] = n//3
    
    n += 1

print(D[N])
trace = [N]
next = pre[N]
for _ in range(D[N]):
    trace.append(next)
    next = pre[next]

print(' '.join(map(str, trace)))