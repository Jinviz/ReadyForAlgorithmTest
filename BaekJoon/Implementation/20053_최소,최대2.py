N = int(input())

for _ in range(N):
    T = int(input())
    case = list(map(int, input().split()))
    print(min(case), max(case))