# 1. 전체출력
# 2. 테두리 출력
# 3. 전체 출력(안쪽)
# 4. 테두리 출력
# 5. 1번부터 반복 
# 6. 이전 출력 

N = int(input())
n = N*4-3
star = "*"
space = " "

def recursion(turn):
    border_left = (star+space)*turn
    border_right = (space+star)*turn

    print(border_left + star*(n-4*turn) + border_right)
    if(turn == N-1):
        return
    print(border_left + star+space*(n-4*turn-2)+star + border_right)
    recursion(turn+1)
    print(border_left + star+space*(n-4*turn-2)+star + border_right)
    print(border_left + star*(n-4*turn) + border_right)

recursion(0)
