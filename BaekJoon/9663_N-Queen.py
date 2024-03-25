# 체스 N개가 놓일 수 있는 영역 선택 + 서로 잡을 수 없는 위치의 조건 
N = int(input())
def backtracking(cnt, current, visited):
    global case
    if cnt == N-1:
        case += 1
    else:
        # 해당 보드영역 방문 처리
        removeArea(cnt, current, visited)
        for i in visited:
            print(i)
        print("")
        for i in range(N):
            if visited[cnt+1][i] != 1:
                backtracking(cnt+1, i, visited)

# 퀸의 이동반경을 케이스에서 제외시키기
def removeArea(count, start, board):
    for i in range(N):
        board[i][start] = 1
        board[count][i] = 1
        if 0 <= count-i < N and 0 <= start-i < N:
            board[count-i][start-i] = 1
        if 0 <= count-i < N and 0 <= start+i < N:
            board[count-i][start+i] = 1
        if 0 <= count+i < N and 0 <= start-i < N:
            board[count+i][start-i] = 1
        if 0 <= count+i < N and 0 <= start+i < N:
            board[count+i][start+i] = 1

case = 0    
visit_board = [[0 for _ in range(N)] for _ in range(N)]   # 중복과 순서없이 체스 N개가 놓일 수 있는 체스판 영역 선택

for n in range(N):
    board = [row[:] for row in visit_board]
    backtracking(0, n, board)

print(case)