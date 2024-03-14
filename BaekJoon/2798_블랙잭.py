n, m = map(int, input().split())
card = list(map(int, input().split()))
sum = []
for a in range(n-2):
    for b in range(a+1, n-1):
        for c in range(b+1, n):
            dump = card[a]+card[b]+card[c]
            if(dump <= m):
                sum.append(dump)

print(max(sum))
