# 체스 N개가 놓일 수 있는 영역 선택 + 서로 잡을 수 없는 위치의 조건 
from itertools import combinations

N = int(input())
visit = [[0 for _ in range(N)] for _ in range(N)]# 중복과 순서없이 체스 N개가 놓일 수 있는 체스판 영역 선택
count = 0
direction = [-1,0,1]
case = []
def backtracking(current, cnt, visit):
    if cnt == N:
        return visited
    # 해당 보드영역 방문 처리
    a, b = divmod(current, N)
    visited = visit
    visited[a][b] = 1
    
    for dx in direction:
        for dy in direction:
            if 0 <= a+dx < N and 0 <= b+dy < N: # 보드판 벗어나기 방지
                if dx != 0 and dy != 0: # 제자리 머물기 제외
                    if visited[a+dx][b+dy] == 0:    # 방문한 영역 제외
                        backtracking(N*(a+dx)+b+dy, cnt+1, visited)

for n in range(N):
    case.append(backtracking(n,0,visit))

result = set(case)
print(len(result))


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