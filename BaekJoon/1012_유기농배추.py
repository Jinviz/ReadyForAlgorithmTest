from collections import deque

# M[n]: 가로 / N[n]: 세로 / total_location[n]: (m,n)위치 정보 리스트
case = int(input())
total_location= []    # 케이스별 벌레 위치값(튜플)로 이루어진 리스트 저장
m, n = [], []

for _ in range(case):
    a, b, c = map(int, input().split())
    m.append(a)
    n.append(b)
    cabbage = [tuple(map(int, input().split())) for _ in range(c)]
    total_location.append(cabbage)

# 케이스별 M x N 땅(total_ground) 빈 리스트 생성 
total_ground = []
for c in range(case): 
    dump = [[0 for _ in range(m[c])] for _ in range(n[c])]
    total_ground.append(dump)

# 빈 total_ground에 배추 위치 표시
for c in range(case):
    for point in total_location[c]:
        total_ground[c][point[1]][point[0]] = 1 

dx = [1,-1,0,0]
dy = [0,0,1,-1]
total_count = [0 for _ in range(case)]

# DFS 검사
for state in range(case):
    ground = total_ground[state]
    x = m[state]
    y= n[state]

    for b, row in enumerate(ground):
        for a, element in enumerate(row):
            if element == 1:
                queue = deque([(a,b)])
                while queue:
                    start = queue.popleft()
                    for d in range(4):
                        nx = start[0] + dx[d]
                        ny = start[1] + dy[d]
                        if 0 <= nx < x and 0 <= ny < y and ground[ny][nx] == 1:
                            ground[ny][nx] = 0  # 방문 처리
                            queue.append((nx,ny))
                total_count[state] += 1
        

for n in range(case):
    print(total_count[n])
