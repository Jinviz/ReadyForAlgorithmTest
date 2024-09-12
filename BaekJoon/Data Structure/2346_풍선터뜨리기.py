from collections import deque
import sys

input = sys.stdin.readline
N = int(input())
balloons = list(map(int, input().split()))
# print(balloons)
next = 0
result = []

def next_cal(n):
    global next
    result.append(n+1)
    if balloons[n] < 0:
        next = len(balloons)-(abs(balloons[n]) % len(balloons))
        balloons.pop(n)
    else:
        next = balloons[n] % len(balloons) 
        balloons.pop(n)

next_cal(0)

for i in range(N-1):
    next_cal(next)
    # print(result)
    
