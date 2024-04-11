from collections import deque

N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]

count = [[1 for _ in range(M)] for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]
dxdy = [(0,1),(1,0),(-1,0),(0,-1)]
queue = deque([(0,0)])

while queue:
    x, y = queue.popleft()
    for d in dxdy:
        nx, ny = x + d[0], y + d[1]
        if 0 <= nx < N and 0 <= ny < M:
            if maze[nx][ny] == 1 and visited[nx][ny] == False:
                queue.append((nx,ny))
                visited[nx][ny] = True
                count[nx][ny] = count[x][y] + 1

print(count[N-1][M-1])

