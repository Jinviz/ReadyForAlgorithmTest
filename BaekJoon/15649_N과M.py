N, M = map(int, input().split())
number = [str(n) for n in range(1,N+1)]

def progression(case, num):
    if len(case) == M:
        result = " ".join(case)
        print(result)
        case.pop()
        return
    
    for n in num:
        print(n)
        case.append(n)
        num_list = num[:]
        num_list.remove(n)
        progression(case, num_list)
        print("end")

progression([], number)

# def dfs():
#     if len(s) == m:
#         print(' '.join(map(str, s)))
#         return
#     for i in range(1, n+1):
#         if visited[i]:
#             continue
#         visited[i] = True
#         s.append(i)
#         dfs()
#         s.pop()
#         # print(s)
#         # print(visited)
#         visited[i] = False
            

# n, m = map(int, input().split())
# s = []
# visited = [False] * (n+1)

# dfs()
        
    