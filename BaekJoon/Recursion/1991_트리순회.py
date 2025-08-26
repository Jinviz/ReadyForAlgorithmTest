# N = int(input())
# V = [list(input().split()) for _ in range(N)]
# dot = '.'
# graph = {}

# for v in V:
#     graph[v[0]] = (v[1],v[2])

# # preorder, inorder, postorder = '','',''
# visited = [False for _ in range(len(graph))]

# def preorder_traversal(v, preorder):
#     for g in v:
#         if g[1] == dot:
#             preorder += list(g.keys())[0]
#             break
#         else: 
#             preorder_traversal(preorder)



# preorder_traversal(graph, '')

# import sys

# input = sys.stdin.readline

# N = int(input().strip())
# tree = {}
# none_node = '.'

# for _ in range(N):
#     p, l, r = input().split()
#     tree[p] = (l, r)

# def preorder(node, out):
#     left_node = tree[node][0]
#     right_node = tree[node][1]
#     out.append(node)

#     if left_node != none_node:
#         preorder(left_node, out)
#     if right_node != none_node:
#         preorder(right_node, out)

#     return out

# def inorder(node, out):
#     left_node = tree[node][0]
#     right_node = tree[node][1]

#     if left_node != none_node:
#         inorder(left_node, out)
#     out.append(node)
#     if right_node != none_node:
#         inorder(right_node, out)

#     return out

# def postorder(node, out):
#     left_node = tree[node][0]
#     right_node = tree[node][1]

#     if left_node != none_node:
#         postorder(left_node, out)
#     if right_node != none_node:
#         postorder(right_node, out)
#     out.append(node)

#     return out

# pre, ino, post = [], [], []
# root = 'A'

# preorder(root, pre)
# inorder(root, ino)
# postorder(root, post)

# print(''.join(pre))
# print(''.join(ino))
# print(''.join(post))

import sys
input = sys.stdin.readline

N = int(input().strip())
tree = {}

for _ in range(N):
    p, l, r = input().split()
    tree[p] = (l, r)

pre, ino, post = [], [], []

def preorder(node: str):
    if node == '.':
        return
    pre.append(node)
    l, r = tree[node]
    preorder(l)
    preorder(r)

def inorder(node: str):
    if node == '.':
        return
    l, r = tree[node]
    inorder(l)
    ino.append(node)
    inorder(r)

def postorder(node: str):
    if node == '.':
        return
    l, r = tree[node]
    postorder(l)
    postorder(r)
    post.append(node)

root = 'A'  # 항상 A가 루트
preorder(root)
inorder(root)
postorder(root)

print(''.join(pre))
print(''.join(ino))
print(''.join(post))
