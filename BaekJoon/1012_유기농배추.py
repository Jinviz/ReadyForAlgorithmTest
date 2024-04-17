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
    cabbage = [tuple(map(int, input().split())) for _ in range(c)]
    location.append(cabbage)

# 케이스별 M x N 땅(total_ground) 빈 리스트 생성 
total_ground = []
for c in range(case): 
    dump = [[0 for _ in range(m[c])] for _ in range(n[c])]
    total_ground.append(dump)

# 빈 total_ground에 배추 위치 표시
for c in range(case):
    for point in location[c]:
        total_ground[c][point[1]][point[0]] = 1 


# 방문 리스트 생성 / 길이: 튜플로 이루어진 리스트의 길이
visited = []
for n in range(case):
    visit = [0 for _ in range(len(location[n]))]
    visited.append(visit)

dx = [1,-1,0,0]
dy = [0,0,1,-1]

# DFS 검사
for state in range(case):
    cabbage = location[state][0]
    ground = total_ground[state]
    queue = deque([ground[]])    # cabbageList[0] = (x,y) 튜플타입

    while queue:
        for n in range(4):


        
