# 양방향 조건 (그래프)
# 작은 숫자 먼저 방문

from collections import deque

info = list(map(int, input().split()))
graph = [[] for _ in range(info[0]+1)]
link_info = [list(map(int, input().split())) for _ in range(info[1])]

for link in link_info:
    graph[link[0]].append(link[1])
    graph[link[1]].append(link[0])
    graph[link[0]].sort()
    graph[link[1]].sort()

bfs_visited, dfs_visited = [False for _ in range(info[0]+1)],[False for _ in range(info[0]+1)] 

# dfs
def dfs(g, start, visited):
    visited[start] = True
    print(start, end= ' ')

    for node in g[start]: 
        if visited[node] == False:
            dfs(g, node, visited)
# bfs
def bfs(g, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end= ' ')
        for i in g[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

dfs(graph, info[2], dfs_visited)
print()
bfs(graph, info[2], bfs_visited)

