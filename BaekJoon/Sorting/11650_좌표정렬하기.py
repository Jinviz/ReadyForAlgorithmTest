import sys

N = int(input())
dot = [tuple(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

dot.sort(key=lambda x: (x[0],x[1]))

for n in range(N):
  print(dot[n][0], dot[n][1])
