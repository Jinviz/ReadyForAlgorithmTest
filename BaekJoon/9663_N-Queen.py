from itertools import combinations

N = int(input())
board_num = []
for i in range(N*N):
    board_num.append(i)
num = combinations(board_num, N)

board = [[0] *N] *N 

# 퀸의 활동 영역 1로 처리
board[num/N][num%N] = 1

# 칠해야할 영역에 1이 있는 지 확인
for i in range(N):
    # i가 범위를 넘지않는 경우를 구해야 함
    if board[num/N -i][num%N -i] == 1 or board[num/N -i][num%N +i] == 1 or board[num/N +i][num%N -i] == 1 or board[num/N +i][num%N +i] == 1:
        break
    board[num/N -i][num%N -i], board[num/N -i][num%N +i], board[num/N +i][num%N -i], board[num/N +i][num%N +i] = 1, 1, 1, 1