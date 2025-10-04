import sys
input = sys.stdin.readline

N,M = map(int,input().split())
dx, dy = [-1,0,1,0,-1,0,1,0], [0,1,0,-1,0,1,0,-1]
result = []
office = []
cctv_list = []

# 사무실 모습, CCTV 위치 저장
for m in range(N):
    row = list(map(int, input().split()))
    office.append(row)

    for n, cell in enumerate(row):
        if cell != 0 and cell != 6:
            cctv_list.append((m,n))

# 사각지대 계산
def calculate_square_area(board):
    cnt = 0
    for row in board:
        cnt += row.count(0)
    return cnt

# 감시 영역 체크
def paint(i,x,y,board):
    nx, ny = x, y
    while(1):
        nx += dx[i]
        ny += dy[i]

        if not(0 <= nx < N and 0 <= ny < M):
            break

        if board[nx][ny] == 6:
            break

        if board[nx][ny] == 0:
            board[nx][ny] = 7

# 감시 영역 계산
def calculate_cctv(idx, board):
    if idx >= len(cctv_list):
        global result
        result.append(calculate_square_area(board))
        return
    x,y = cctv_list[idx]
    cctv = office[x][y]

    if(cctv == 1):
        for i in range(4):
            board2 = [list(row) for row in board]
            paint(i,x,y,board2)
            calculate_cctv(idx+1, board2)

    if(cctv == 2):
        for i in range(2):
            board2 = [list(row) for row in board]
            paint(i,x,y,board2)
            paint(i+2,x,y,board2)
            calculate_cctv(idx+1, board2)

    if(cctv == 3):
        for i in range(4):
            board2 = [list(row) for row in board]
            paint(i,x,y,board2)
            paint(i+1,x,y,board2)
            calculate_cctv(idx+1, board2)

    if(cctv == 4):
        for i in range(4):
            board2 = [list(row) for row in board]
            paint(i,x,y,board2)
            paint(i+1,x,y,board2)
            paint(i+2,x,y,board2)
            calculate_cctv(idx+1, board2)

    if(cctv == 5):
        board2 = [list(row) for row in board]
        for i in range(4):
            paint(i,x,y,board2)
        calculate_cctv(idx+1, board2)

calculate_cctv(0, office)

print(min(result))