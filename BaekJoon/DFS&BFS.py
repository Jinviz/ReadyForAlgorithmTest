# dfs
N = int(input())
node_list = [list(map(int, input().split())) for _ in range(N)]

def dfs(g, v, visited):
    visited[v] = True
    print(v, end=' ')
    for node in g[v]:
        if visited[node] == False:
            dfs(g, node, visited)

visited = [False for _ in range(N+1)]
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

visited = [False for _ in range(N+1)]
bfs(node_list, 1, visited)

# *** 간단한 구현 ***
graph = {
    1: [2, 3],
    2: [4, 5],
    3: [6],
    4: [],
    5: [6],
    6: []
}
# dfs
visited = set()

def dfs(node):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbor in graph[node]: # 이웃이 1개일 수도 2개일 수도 있기 때문에 for문으로 돌리는 게 일반적임
            dfs(neighbor)
dfs(1)

# bfs
from collections import deque

graph = {
    1: [2, 3],
    2: [4, 5],
    3: [6],
    4: [],
    5: [6],
    6: []
}

def bfs(start):
    visited = set([start])
    queue = deque([start])

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
bfs(1)
