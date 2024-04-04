# N = int(input())
# node_list = [list(map(int, input().split())) for _ in range(N)]

# def dfs(g, v, visited):
#     visited[start] = True
#     print(v, end=' ')
#     for node in g[v]:
#         if visited[node] == False:
#             dfs(g, node, visited)

# visited = [False for _ in range(N)]
# dfs(node_list, 1, visited)


from collections import deque/