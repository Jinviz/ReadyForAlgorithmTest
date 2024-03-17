row, column = map(int, input().split())
board = [list(input()) for _ in range(row)]

start = ['BW', 'WB']
b_case, w_case = [[''.join([s[0] if (i+j) % 2 == 0 else s[1] for j in range(column)]) for i in range(row)] for s in start]  # 체스판 생성 (시작이 B 이거나 W)
b_count, w_count = [[[0 for _ in range(column)] for _ in range(row)] for _ in range(2)]
b_sum, w_sum = [[[0 for _ in range(column)] for _ in range(row)] for _ in range(2)]
min_case = row * column

for i in range(row):
    for j in range(column):
        if board[i][j] != b_case[i][j]:
            b_count[i][j] = 1
        elif board[i][j] != w_case[i][j]:
            w_count[i][j] = 1
    

for a in range(row-7):
    for b in range(column-7):
        b_temp = 0
        w_temp = 0 
        for i in range(0,8):
            for j in range(0,8):
                b_temp += b_count[a+i][b+j]
                w_temp += w_count[a+i][b+j]
        min_case = min(min_case, b_temp, w_temp)
        
print(min_case)

