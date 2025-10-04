import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [0 for _ in range(N)]

for _ in range(M):
    start,end,num = map(int,input().split())
    for i in range(start-1, end):
        arr[i] = num

print(' '.join(map(str, arr)))