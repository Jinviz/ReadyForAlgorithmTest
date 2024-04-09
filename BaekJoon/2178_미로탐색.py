from collections import deque
dxdy = [(1,0),(0,1),(-1,0),(0,-1)]
# dx = [-1, 1, 0, 0]
# dy = [0, 0 ,-1, 1]

N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]

def dfs(n, m, visited, cnt):
    visited[n][m] = True
    cnt += 1
    print(cnt)

    if n == N-1 and m == M-1:
        return True

    for d in dxdy:
        nx, ny = n + d[0], m + d[1]
        if n+d[0] < N and m+d[1] < M:
            if maze[nx][ny] == 1 and visited[nx][ny] == False:
                result = dfs(nx, ny, visited, cnt)
                if result == True:
                    return
    
    return cnt

count = dfs(0, 0, visited, 0)
print(count)
