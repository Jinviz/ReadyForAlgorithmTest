import sys 

input = sys.stdin.readline
n = int(input())

sequence = [int(input()) for _ in range(n)]
items = [item+1 for item in range(n)]
stk = [0]
output = []

for s in sequence:
    while stk[-1] != s:
        if len(items) == 0:
            output.append('NO')
            break
        stk.append(items[0])
        output.append('+')        
        items.pop(0)
    stk.pop()
    output.append('-')

if 'NO' in output:
    print('NO')
else:
    for out in output:
        print(out)