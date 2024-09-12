from collections import deque
import sys

input = sys.stdin.readline
N = int(input())
balloons = list(map(int, input().split()))
next = 0
result = []

def next_cal(n):
    cal = (n + balloons[n])
    result.append(balloons.pop(n))
    if cal < 0:
        next = len(balloons)-(abs(cal) % len(balloons)) - 1 
    else:
        next = cal % len(balloons)

next_cal(0)

for i in range(N-1):
    next_cal(result[-1])
    print(result)
    
