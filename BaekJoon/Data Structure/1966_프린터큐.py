from collections import deque
import sys

input = sys.stdin.readline
case = int(input())

for _ in range(case):
    count = 1
    N, M = map(int, input().split())
    sequence = list(map(int, input().split()))
    queue = deque(list(n for n in enumerate(sequence)))
    while len(queue) > 0:
        if queue[0][1] == max(sequence):
            if queue[0][0] == M:
                print(count)
            queue.popleft()
            sequence.remove(max(sequence))
            count += 1
        else:
            queue.rotate(-1)
            
