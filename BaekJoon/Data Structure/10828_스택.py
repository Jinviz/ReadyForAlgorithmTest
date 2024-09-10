import sys

N = int(input())
stack = []

for _ in range(N):
    command = sys.stdin.readline().split()[-1]
    if command == 'pop':
        print(stack.pop(-1) if len(stack) > 0 else -1)
    elif command == 'size':
        print(len(stack))
    elif command == 'empty':
        print(1 if len(stack) == 0 else 0)
    elif command == 'top':
        print(stack[-1] if len(stack) > 0 else -1)
    else:   
        stack.append(command)