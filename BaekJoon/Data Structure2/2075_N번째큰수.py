import sys

N = int(input())
rows = list()
while True:
    row = map(int, sys.stdin.readline().rstrip().split())
    if row:
        rows.append(row)
    else: break

squence = [0]
for n in range(N):
    for row in rows:
        if squence[n] < max(row):
            squence[n] = max(row)
    
    for i, row in enumerate(rows):
        if squence[n] == max(row):
            rows[i].remove(max(row))
    
print(squence[-1])
