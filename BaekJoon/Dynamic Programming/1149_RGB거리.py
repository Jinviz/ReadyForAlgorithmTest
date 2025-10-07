import sys
input = sys.stdin.readline

N = int(input())
R, G, B = [], [], []
for _ in range(N):
    r, g, b = map(int, input().split())
    R.append(r)
    G.append(g)
    B.append(b)

D = [[0,0,0] for _ in range(len(R))]
D[0][0] = R[0]
D[0][1] = G[0] 
D[0][2] = B[0] 

for n in range(1,N):
    D[n][0] = R[n]+min(D[n-1][1], D[n-1][2])
    D[n][1] = G[n]+min(D[n-1][0], D[n-1][2])
    D[n][2] = B[n]+min(D[n-1][0], D[n-1][1])

print(min(D[N-1]))

# 백트래킹 풀이 (시간초과)
# import sys
# input = sys.stdin.readline

# N = int(input())
# costs = [list(map(int,input().split())) for _ in range(N)]

# result = []

# def calculate_cost(ctn, sum, rule):
#     for idx, cost in enumerate(costs[ctn]):
#         if idx != rule:
#             if ctn == len(costs)-1:
#                 global result
#                 result.append(sum+cost)
#             else:
#                 calculate_cost(ctn+1, sum+cost, idx)

# calculate_cost(0, 0, -1)

# print(min(result))