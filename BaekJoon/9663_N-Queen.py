# 체스 N개가 놓일 수 있는 영역 선택 + 서로 잡을 수 없는 위치의 조건 
N = int(input())
def backtracking(cnt, visited):
    global case
    if cnt == N:
        case += 1
        return 
    
    for i in range(N):
        if safeArea(cnt, i, visited):
            visited[cnt][i] = 1
            backtracking(cnt + 1, visited)
            visited[cnt][i] = 0

# 퀸의 이동반경을 케이스에서 제외시키기
def safeArea(row, col, board):
    for i in range(N):
        # 수직 방향
        if board[i][col] == 1:
            return False
        # 왼쪽 위 대각선 방향
        if 0 <= row-i < N and 0 <= col-i < N:
            if board[row-i][col-i] == 1:
                return False
        # 오른쪽 위 대각선 방향
        if 0 <= row-i < N and 0 <= col+i < N:
            if board[row-i][col+i] == 1:
                return False
    
    return True

case = 0    
visit_board = [[0 for _ in range(N)] for _ in range(N)]   # 중복과 순서없이 체스 N개가 놓일 수 있는 체스판 영역 선택

backtracking(0, visit_board)
