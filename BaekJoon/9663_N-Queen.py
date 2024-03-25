# 체스 N개가 놓일 수 있는 영역 선택 + 서로 잡을 수 없는 위치의 조건 
from itertools import combinations

N = int(input())
visit = [[0 for _ in range(N)] for _ in range(N)]   # 중복과 순서없이 체스 N개가 놓일 수 있는 체스판 영역 선택
case = []
def backtracking(current, cnt, visited):
    if cnt == N:
        if visited not in case:
            case.append(visited)
        return 
    # 해당 보드영역 방문 처리
    a, b = current
    board = removeArea(a, b, visited)
    
    for i in range(N):
        for j in range(N):
            if board[i][j] != 1:
                backtracking((i,j), cnt+1, [row[:] for row in board])

# 퀸의 이동반경을 케이스에서 제외시키기
def removeArea(x, y, board):
    for i in range(N):
        board[i][y] = 1
        board[x][i] = 1
        if 0 <= x-i < N and 0 <= y-i < N:
            board[x-i][y-i] = 1
        if 0 <= x-i < N and 0 <= y+i < N:
            board[x-i][y+i] = 1
        if 0 <= x+i < N and 0 <= y-i < N:
            board[x+i][y-i] = 1
        if 0 <= x+i < N and 0 <= y+i < N:
            board[x+i][y+i] = 1

        return board
    
for n in range(N*N):
    a, b = divmod(n, N)
    backtracking((a,b),0,visit)

print(len(case))
