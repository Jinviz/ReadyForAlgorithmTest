# dfs
N = int(input())
node_list = [list(map(int, input().split())) for _ in range(N)]

def dfs(g, v, visited):
    visited[start] = True
    print(v, end=' ')
    for node in g[v]:
        if visited[node] == False:
            dfs(g, node, visited)

visited = [False for _ in range(N)]
dfs(node_list, 1, visited)

# bfs
from collections import deque
N = int(input())
node_list = [list(map(int, input().split())) for _ in range(N)]

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
	
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

visited = [False for _ in range(N)]
bfs(node_list, 1, visited)