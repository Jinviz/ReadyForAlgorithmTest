from collections import deque
N = int(input())
ground = [list(map(int, input())) for _ in range(N)]
town = 0    # 단지 수
town_house = [] #단지별 숫자
dx = [1,-1,0,0]
dy = [0,0,1,-1]

# 인덱스로 접근해야 하는지?
# 방문 처리를 따로 리스트를 만드는지?

# 섹션별로 bfs를 굴린다는 구조
for n in range(N):
    for m in range(N):
        if ground[n][m] == 1:
            queue = deque([(n,m)])
            ground[n][m] = 0
            town += 1                   # 단지 숫자 추가
            town_house.append(1)        # 단지의 집 개수에 대한 정보
            while queue:
                x, y = queue.popleft()
                for i in range(4):
                    nx, ny = x+dx[i], y+dy[i]
                    if 0 <= nx < N and 0 <= ny < N and ground[nx][ny] == 1:
                        queue.append((nx,ny))
                        ground[nx][ny] = 0      # 방문 처리
                        town_house[-1] += 1     # 단지 내의 집 개수 추가 

print(town)
for house in sorted(town_house):
    print(house)