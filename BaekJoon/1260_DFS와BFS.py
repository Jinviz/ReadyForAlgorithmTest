from collections import deque

info = list(map(int, input().split()))
graph = [[] for _ in range(info[0]+1)]
link_info = [list(map(int, input().split())) for _ in range(info[1])]

for l in link_info:
    graph[l[0]].append(l[1])

bfs_visited, dfs_visited = [False, False for _ in range(info[0])] * 2
bfs_result, dfs_result = [] * 2

# dfs
def dfs(g, start, visited):
    visited[start] = True
    bfs_result.append(start)

    for node  in g[start]: 
        if visited[node] == False:
            bfs(g, node, visited)

# bfs
def bfs(g, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        bfs_result.append(v)

# 낮은 순서대로 접근은 오름차순 정렬 내장함수 사용해야 함