# dfs bfs 둘다 풀이 가능
# dfs 풀이
from collections import deque

computer = int(input())
linked_num = int(input())
linked_node = [list(map(int, input().split())) for _ in range(linked_num)]
graph = [[] for _ in range(computer+1)]
visited = [False for _ in range(computer+1)]

count = 0

for link in linked_node:
    graph[link[0]].append(link[1])
    graph[link[1]].append(link[0])

def bfs(g, start, visited):
    global count
    visited[start] = True
    queue = deque([start])

    while queue:
        v = queue.popleft()
        count += 1
        for i in g[v]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True

bfs(graph, 1, visited)
print(count-1)