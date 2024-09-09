from collections import deque
import sys

queue = deque([])
N = int(input())

for _ in range(N):
    command = sys.stdin.readline().split()[-1]
    if command == 'pop':
        print(queue.popleft() if len(queue) > 0 else -1)
    elif command == 'size':
        print(len(queue))
    elif command == 'empty':
        print(1 if len(queue) == 0 else 0)
    elif command == 'front':
        print(queue[0] if queue[0] else -1)
    elif command == 'back':
        print(queue[-1] if queue[-1] else -1)
    else:   
        queue.append(command)