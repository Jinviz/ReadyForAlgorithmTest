# 체스 N개가 놓일 수 있는 영역 선택 + 서로 잡을 수 없는 위치의 조건 
from itertools import combinations

N = int(input())
board_num = []
for i in range(N*N):
    board_num.append(i)
num = list(combinations(board_num, N)) # 중복과 순서없이 체스 N개가 놓일 수 있는 체스판 영역 선택
print(num)
# board = [[0] *N] *N 

# # 퀸의 활동 영역 1로 처리
# board[num/N][num%N] = 1


# 조합 경우의 수




# # 칠해야할 영역에 1이 있는 지 확인
# for i in range(N):
#     # i가 범위를 넘지않는 경우를 구해야 함

#     # 대각선 방향 체크
#     if board[num/N -i][num%N -i] == 1 or board[num/N -i][num%N +i] == 1 or board[num/N +i][num%N -i] == 1 or board[num/N +i][num%N +i] == 1:
#         break
#     # 일자 방향 체크
#     elif board[num/N -i][num%N] == 1 or board[num/N + i][num%N] == 1 or board[num/N][num%N -i] == 1 or board[num/N][num%N +i] == 1:
#         break


#     # 대각선 방향 
#     board[num/N -i][num%N -i], board[num/N -i][num%N +i], board[num/N +i][num%N -i], board[num/N +i][num%N +i] = 1, 1, 1, 1