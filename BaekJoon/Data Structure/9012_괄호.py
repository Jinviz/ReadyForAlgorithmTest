import sys

N = int(input())

for _ in range(N):
    input = sys.stdin.readline().rstrip()
    same = 0
    for n in range(len(input)):
        if same < 0:
            break
        if input[n] == '(':
            same += 1
        else:
            same -= 1
    print('YES' if same == 0 else 'NO')