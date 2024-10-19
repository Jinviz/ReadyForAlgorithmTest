board = list(list(input().split()) for _ in range(5))
bingo = list(list(0 for _ in range(5)) for _ in range(5))
call = list(list(input().split()) for _ in range(5))
sequence = list(b for a in call for b in a)
count = 0

def check_line_bingo():
    for i in range(5):
        global count
        # 가로 빙고 검사
        count += 1 if 0 not in bingo[i] else 0
        
        # 세로 빙고 검사
        column_bingo = True
        for j in range(5):
            if bingo[j][i] == 0:
                column_bingo = False
                break
        count += 1 if column_bingo else 0 # 세로 빙고면 빙고 카운트
        
def check_diagonal_bingo():
    global count
    r_diagonal_bingo = 0
    l_diagonal_bingo = 0
    for i in range(5):
        # 대각선 빙고 검사 (2case)
        # 00 11 22 33 44  / 04 13 22 31 40
        r_diagonal_bingo += 1 if bingo[i][i] == 1 else 0 ## 왼쪽시작대각선
        l_diagonal_bingo += 1 if bingo[i][4-i] == 1 else 0 ## 오른쪽시작대각선
    count += 1 if r_diagonal_bingo == 5 else 0
    count += 1 if l_diagonal_bingo == 5 else 0

        

for number in sequence:
    x,y = 0,0
    for a in range(5):
        if number in board[a]:
            y = board[a].index(number)
            x = a
            break
    bingo[x][y] = 1
    check_line_bingo()            
    check_diagonal_bingo()     
    if count >= 3:
        print(sequence.index(number)+1)
        break
    else:
        count = 0
