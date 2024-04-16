from collections import deque

# M[n]: 가로 / N[n]: 세로 / location[n]: (m,n)위치 정보 리스트
case = int(input())
location= []    # 케이스별 벌레 위치값(튜플)로 이루어진 리스트 저장
m, n, k = [], [], []

for _ in range(case):
    a, b, c = map(int, input().split())
    m.append(a)
    n.append(b)
    k.append(c)
    cabbage = [tuple(map(int, input().split())) for _ in range(k)]
    location.append(cabbage)

# 케이스별 M x N 땅(ground) 빈 리스트 생성 
ground = []
for c in range(case): 
    dump = [[0 for _ in range(m[c])] for _ in range(n[c])]
    ground.append(dump)

# 빈 ground에 배추 위치 표시
for c in range(case):
    for point in location[c]:
        ground[c][point[1]][point[0]] = 1 

            


dx = [1,-1,0,0]
dy = [0,0,1,-1]



for state in range(case):
    for 
    queue = deque([(0,0)])
    while queue:
