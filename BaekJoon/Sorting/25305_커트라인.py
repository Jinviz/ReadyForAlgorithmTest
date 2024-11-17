import sys

N, K = map(int, input().split())
score = list(map(int, sys.stdin.readline().split()))

score.sort()

print(score[N-K])
