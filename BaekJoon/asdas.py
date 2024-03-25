N = int(input())

def backtracking(cnt, visited):
    global case
    if cnt == N:
        case += 1
        return
    for i in range(N):
        if is_safe(cnt, i, visited):
            visited[cnt][i] = 1
            backtracking(cnt + 1, visited)
            visited[cnt][i] = 0

def is_safe(row, col, board):
    for i in range(row):
        if board[i][col] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 1:
            return False
    return True

case = 0    
visit_board = [[0 for _ in range(N)] for _ in range(N)]

backtracking(0, visit_board)

print(case)
